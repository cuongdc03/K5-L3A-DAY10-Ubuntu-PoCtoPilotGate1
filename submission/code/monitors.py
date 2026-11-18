"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def _tracking_delay_by_parcel(trial):
    """parcel_id -> số ngày trễ theo tracking DB, đọc từ event `tracking` của chính trial."""
    out = {}
    for ev in trial.get("events") or []:
        if isinstance(ev, dict) and ev.get("type") == "tracking":
            for p in ev.get("parcels") or []:
                if isinstance(p, dict):
                    out[p.get("parcel_id")] = p.get("delay")
    return out


def _fault_parcel_id(row):
    """fault_rows là dict; chấp nhận cả dạng [carrier_id, parcel_id] cho an toàn."""
    if isinstance(row, dict):
        return row.get("parcel_id")
    if isinstance(row, (list, tuple)) and len(row) >= 2:
        return row[1]
    return None


def carrier_fault_on_zero_delay_rate(trials):
    """Tỉ lệ lỗi hãng bị ghi cho kiện mà tracking ghi trễ ĐÚNG 0 ngày.

    Không dùng nhãn: chỉ đọc event `tracking` (parcels[].parcel_id, parcels[].delay)
    và các dòng đã ghi vào `faults`. Mẫu số là số dòng lỗi hãng đã ghi; dòng không tra
    được parcel trong tracking vẫn nằm ở mẫu số nhưng không vào tử số.
    Không có dòng lỗi nào -> trả 0.0.
    """
    bad = total = 0
    for t in trials:
        delays = _tracking_delay_by_parcel(t)
        for row in t.get("faults") or []:
            total += 1
            if delays.get(_fault_parcel_id(row)) == 0:
                bad += 1
    return bad / total if total else 0.0


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "carrier_fault_on_zero_delay_rate": carrier_fault_on_zero_delay_rate,   # vòng 2: bắt lỗi hãng oan khi kiện không trễ
}
STARTER_MONITORS = ("escalation_rate",)
