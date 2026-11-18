"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def pre_guard(ctx):
    return Verdict.allow()


def _ambiguous_late_parcels(ctx, order):
    if ctx.ticket.get("parcel_id"):
        return False
    return sum(H.db_delay_days(parcel, ctx.as_of) > 0 for parcel in order["parcels"]) >= 2


def write_gate(ctx, action):
    if action["tool"] == "issue_refund":
        existing = ctx.tools.ledger_rows(
            ticket_id=action["ticket_id"],
            order_id=action["order_id"],
        )
        if existing:
            return Verdict.deny("Đã có khoản hoàn cho ticket và đơn này")

        order = ctx.tools.lookup_order(action["order_id"])
        policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
        if not order or not order["parcels"] or policy is None:
            return Verdict.escalate("Thiếu tracking hoặc chính sách để kiểm tra khoản hoàn")

        if _ambiguous_late_parcels(ctx, order):
            return Verdict.escalate("Hai kiện trễ, chưa rõ lỗi của hãng nào")

        requested_parcel = ctx.ticket.get("parcel_id")
        if requested_parcel and not any(
            parcel["parcel_id"] == requested_parcel for parcel in order["parcels"]
        ):
            return Verdict.escalate("Kiện được chỉ định không thuộc đơn hàng")

        parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
        delay_days = H.db_delay_days(parcel, ctx.as_of)
        entitlement = H.entitlement_vnd(
            policy, order, delay_days, parcel.get("delay_cause")
        )
        if entitlement <= 0:
            return Verdict.deny("Tracking không đủ điều kiện hoàn tiền")
        if action["amount_vnd"] > entitlement:
            return Verdict.escalate("Khoản đề xuất vượt quyền lợi theo tracking")


    if action["tool"] == "file_carrier_fault":
        order = ctx.tools.lookup_order(action["order_id"])
        if not order or not order["parcels"]:
            return Verdict.deny("Không có dữ liệu kiện hàng để ghi lỗi hãng")

        if _ambiguous_late_parcels(ctx, order):
            return Verdict.escalate("Hai kiện trễ, chưa rõ lỗi của hãng nào")

        requested_parcel = ctx.ticket.get("parcel_id")
        if requested_parcel and not any(
            parcel["parcel_id"] == requested_parcel for parcel in order["parcels"]
        ):
            return Verdict.deny("Kiện được chỉ định không thuộc đơn hàng")

        parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
        policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
        delay_days = H.db_delay_days(parcel, ctx.as_of)
        if policy is None or not H.carrier_at_fault(policy, parcel, delay_days):
            return Verdict.deny("Tracking và chính sách chưa đủ căn cứ ghi lỗi hãng")

        carrier_id = parcel["carrier_id"]
        limit = ctx.tools.ops_limits().get("max_auto_strikes_per_carrier_per_day")
        if limit is not None and len(ctx.tools.fault_rows(carrier_id=carrier_id)) >= limit:
            return Verdict.escalate("Hãng đã đạt trần ghi lỗi tự động trong ngày")

        verified = {
            "parcel_id": parcel["parcel_id"],
            "carrier_id": carrier_id,
            "driver_id": parcel.get("driver_id"),
            "delay_days": delay_days,
        }
        if any(action.get(key) != value for key, value in verified.items()):
            return Verdict.modify("Dùng kiện, hãng, tài xế và độ trễ theo tracking", **verified)

    return Verdict.allow()
