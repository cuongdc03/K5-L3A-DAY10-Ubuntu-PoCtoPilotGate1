# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng):Ubuntu
- Lớp: `L3A` 
- Repo của bàn: cuongdc03/K5-L3A-DAY10-Ubuntu-PoCtoPilotGate1
- Thẻ sự cố đã bốc (S1–S8): S6

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên    | MSSV        | Vai | Trưởng nhóm |
| --: | ------------ | ----------- | --- | :---------: |
| 1   | Đỗ Cao Cường | 2A202603612 | Vận hành và pháp lý (trưởng nhóm) | x           |
| 2   | Nguyễn Tuấn Kiệt | 2A202603417 | Kỹ sư cổng #2 (đo và kiểm) |             |
| 3   | Trịnh Công Đức | 2A202603527 | Sản phẩm và kinh doanh |             |
| 4   | Nguyễn Minh Đạt | 2A202603582 | Kỹ sư cổng #1 (viết code) |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Phân công chi tiết (4 người)

Điền tên vào cột "Người" rồi chép vai sang cột "Vai" của bảng thành viên. Quyết định v1 và v2 do **cả bàn** chốt.

| Mã  | Vai                                   | Người        | File / phiếu chính                                                                          |
| --- | ------------------------------------- | ------------ | ------------------------------------------------------------------------------------------- |
| A   | Kỹ sư cổng #1 (viết code)             | Nguyễn Minh Đạt | `lab10/guards.py` (`pre_guard`, `write_gate`)                                               |
| B   | Kỹ sư cổng #2 (đo và kiểm)            | Kiệt         | `lab10/monitors.py`; chạy `eval`, `gate`, `trace`, `grade`                                  |
| C   | Sản phẩm và kinh doanh                | Đức          | `config/acceptance_criteria.json`; `operating_gates.json` mục `business`; Phiếu A           |
| D   | Vận hành và pháp lý (**trưởng nhóm**) | Đỗ Cao Cường | `operating_gates.json` mục `operations`, `legal`; `submission/submission.json`; repo và git |

**Quy tắc git:** chỉ D push các commit quan trọng (ký tiêu chí, chốt vòng 1, nộp bài). Mỗi người chỉ sửa file của mình; trước khi push chạy `git pull --rebase`.

### Phút 0–15 · Cài đặt

- **D:** tạo repo **Private** tên `K5-L3A-DAY10-<TenNhom>-PoCtoPilotGate1`, mời tài khoản team chấm, gắn `upstream`, đặt `git config user.name/email`, điền bảng `TEAM.md`.
- **A, B, C:** clone repo, chạy `python3 -m unittest discover -s tests` (cần `Ran 13 tests … OK`).
- **Cả bàn:** chọn eval card và PRD v1.1 của Lab 9; chốt vai.

### Phút 15–65 · Khối 1: tiêu chí rồi ký · Phiếu A

> **Chưa ai chạy** `eval`**.** Lệnh sẽ từ chối, và ngưỡng phải viết khi chưa biết kết quả.

- **C:** câu 1.1, 1.6; điền `acceptance_criteria.json` (`team` = đúng tên repo, `signed_by`, 5 ngưỡng bắt buộc, `escalation_rate_max`, `business_ops`, `stop_condition`, 4 dòng `decision_rule`); hai câu ranh giới đầu ra. Bám `data/world.json` → `ops_limits`, `ops_facts`; không chép từ file example.
- **D:** câu 1.2 (chị Oanh, chị Hạnh) và 1.4 (telemetry production).
- **B:** câu 1.3 (offline metric cho một bước của agent).
- **A:** đọc code (`guards.py`, `helpers.py`, `docs/guide.md` Phụ lục C), chưa chạy gì.
- **Cả bàn:** câu 1.5 (đọc khoảng tin cậy).
- **Phút 60–65 (C điền xong, D thực hiện):** `python3 -m lab10.criteria sign`, rồi chạy đúng dòng git máy in ra và push. Điền A5. Sau đó không sửa file này nữa.

### Phút 65–115 · Khối 2: đo, rủi ro, cổng vòng 1 · Phiếu B

**65–85 (chưa sửa code/config):**

- **B:** câu 2.1 (`eval` base, `gate`, ghi mã lần chạy) và 2.2 (`trace` `T-002@55`, bảng soát lỗi).
- **C:** câu 2.3 (bản đồ dữ liệu, một ví dụ drift).
- **D:** câu 2.4 (HAZOP ≥ 3 dòng + ≥ 2 dòng ngoài kỹ thuật; checklist 9 nhóm, mỗi dòng một PIC có tên).
- **A:** đọc kết quả base của B, chuẩn bị ý tưởng cổng.
- **Cả bàn:** câu 2.5 (pre-mortem 4 lăng kính; đánh dấu 2–3 lý do thành cổng).

**85–105:**

- **A:** câu 2.6, viết 2–3 cổng dựa trên quy tắc (trần hoàn theo khách và ngày, giới hạn số lần ghi lỗi mỗi hãng, chặn PII gửi bên thứ ba, ghi lỗi phải có nguyên nhân). Không xử lý theo mã ticket hay câu chữ cụ thể.
- **B:** câu 2.7 (hai bước tránh rò rỉ dữ liệu), 2.8 (behavioral test và 2 ticket hiểm); chạy `eval` stage `after` và `unittest` để soi hồi quy cho A.
- **C:** câu 2.9, điền mục `business`, mỗi số kèm một câu lý do từ `world.json`.
- **D:** câu 2.10, điền mục `operations` và `legal`; runbook phần 1–3 và mục Giờ cao điểm khớp các con số đó; `operations.pic` không được để trống.

**105–115:**

- **D:** `python3 -m lab10.checkpoint`, rồi commit và push.
- **B:** `eval --stage prepared`, `gate --run ...`.
- **C:** điền cột v1 ở B8 (một quyết định, ba bằng chứng có mã lần chạy, dòng `decision_rule`, ngày quyết định lại). **Cả bàn** chốt.

### Phút 125–200 · Khối 3: sự cố · Phiếu C

- **D:** `git pull --no-rebase --no-edit --allow-unrelated-histories -X ours upstream main` khi Lab Coach báo; ghi số thẻ vào đầu Phiếu C và `TEAM.md`. Chỉ làm đúng thẻ đã bốc.
- **B:** `python3 -m lab10.grade --incident Sx` **trước khi sửa** (C0, C1); dò ≥ 2 ticket hỏng theo hai kiểu khác nhau (C2); thêm ≥ 1 chỉ số trong `monitors.py` (C8).
- **A:** sửa `guards.py` cho nguyên nhân kỹ thuật (C7); fault tree trước và sau khi sửa (C6, C9).
- **C:** specification (câu 3.2, C5); đọc chi phí, ROI, trần tiền; quyết định phạm vi pilot (`business.pilot_scope`).
- **D:** giả định môi trường (câu 3.3); phần riêng theo thẻ (C3); HAZOP của thẻ (C4); sửa `operations`/`legal` khi nguyên nhân là người hoặc quy trình; risk register (C10); runbook phần 4–5 (C11).
- **Nguyên tắc:** mỗi lần chỉ đổi **một thứ**; chạy lại `eval` bộ `base` để chắc không hồi quy.

### Phút 185–240 · Quyết định v2, demo, nộp

- **C:** viết C12 (cột v2 và ba dòng bắt buộc, có số, nói rõ đổi hay giữ so với v1). **Cả bàn** chốt. Không chọn "Tiếp tục" nếu report còn vượt trần hoặc ngưỡng chưa đạt.
- **D:** điền `submission/submission.json`; chạy `python3 -m lab10.check_submission --collect` tới khi `ĐỦ THÀNH PHẦN`; sau demo trả mọi số đã đổi thử về bản v2, chạy lại lệnh 6 và 7; push.
- **A, B:** demo ba mốc `base · prepared · after`; chuẩn bị ticket hiểm để bàn kia phản biện.
- **Cả bàn:** **mỗi người** viết mục cá nhân (kể cả exit ticket) trong `TEAM.md` và tự nộp link repo trên LMS trước deadline.

### Tránh mất điểm

- Chạy `eval` trước khi ký, hoặc không push ngay sau khi ký.
- Sửa tiêu chí sau khi ký, hoặc sửa `lab10/guards_round1.py`, `config/operating_gates.round1.json`.
- Chặn hết, thu hẹp phạm vi về 0, hoặc xếp quá nhiều người trực.
- `team` trong config và `submission.json` không khớp tên repo; `members` thiếu MSSV (−5 mỗi lỗi).
- Dùng AI cho phần nào thì ghi vào mục cá nhân của người đó.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## DoCaoCuong-2A202603612

### Phần việc phụ trách

Vai D, Vận hành và pháp lý, kiêm trưởng nhóm. Phiếu A câu 1.2, 1.4 và mục A5; Phiếu B câu 2.4 (B4 HAZOP, B5 checklist), câu 2.10 (B7.5 runbook 1–3, B7.6 giờ cao điểm); chốt vòng 1 (lệnh 5); `config/operating_gates.json` mục `operations` và `legal`; `submission/submission.json`; quản lý repo, git và PR.

### Đóng góp cụ thể

- Chia 4 vai và lịch theo mốc giờ, ghi vào `TEAM.md`; thiết lập `origin` / `upstream`.
- Viết mục tiêu nhìn từ chị Hạnh (câu 1.2) và telemetry production cho bước ghi lỗi hãng (câu 1.4: lỗi hãng bị khiếu nại hoặc đảo lại trong 7 ngày, ngưỡng báo động, điểm mù).
- HAZOP vòng 1 trên `file_carrier_fault` (4 dòng kỹ thuật, 5 dòng ngoài kỹ thuật) và checklist 9 nhóm có PIC có tên.
- Runbook phần 1–3 và giờ cao điểm; điền `operations` và `legal` trong config. Chặn hai khóa payload `recipient_contact` và `customer_note` khi gửi hãng, bật `carrier_fault_requires_recorded_cause`.
- Thử 1 và 2 người trực: 1 người cho chi phí 5.165đ/ticket và ROI 0,94 (2 người: 7.473đ, ROI 0,34), mọi ngưỡng đã ký vẫn đạt, nên đặt `reviewers_on_shift` = 1 và sửa runbook cho khớp.
- Chạy `python3 -m lab10.checkpoint` chốt vòng 1; gộp xung đột `form-a-criteria.md` giữ cả cột Offline (Kiệt) và Telemetry.

### Bằng chứng

- Commit `3c3f56c`, `b65d8d0`, `a14b7f0` (PR #4); commit `2047cce` (PR #6, chốt vòng 1, 8 ký tự đầu `15388ffc`).
- Mã lần chạy: `R-base-after-20261118-154443-b0af7a` (2 người trực), `R-base-after-20261118-154554-a23b38` (1 người trực), `R-base-prepared-20261118-154614-a23b38` (mốc prepared).
- Giờ ký tiêu chí `2026-11-18T15:03:46`, commit `a15fe63`.
- Dùng trợ lý AI (Claude Code) để đọc repo, soạn nháp HAZOP, checklist, runbook, giá trị config và xử lý xung đột git; nhóm tự rà soát và chịu trách nhiệm về các con số.

### Exit ticket

Học được rằng nhiều thứ không cần code: một con số trong config (số người trực) đổi ROI từ 0,34 lên 0,94. Còn chưa chắc: thời hạn dừng 15 phút và ngưỡng gọi thêm người có hợp lý ở giờ cao điểm thật hay không, vì bộ nền chỉ có 22 ticket.

## TrinhCongDuc-2A202603527

### Phần việc phụ trách

Vai C — Sản phẩm và kinh doanh: Phiếu A câu 1.1, 1.6; Phiếu B câu 2.3, 2.9; Phiếu C câu 3.2, phần kinh doanh của sự cố và C12; `config/acceptance_criteria.json` và mục `business` trong `config/operating_gates.json`.

### Đóng góp cụ thể

Soạn mục tiêu hệ thống, tiêu chí chấp nhận và quy tắc quyết định; lập bản đồ dữ liệu/trường nguồn sự thật, nêu ví dụ drift chính sách; đề xuất trần chi phí, ROI, ngân sách hoàn và phạm vi pilot dựa trên `data/world.json`. Ở Phiếu C C5, đặc tả điều kiện quy lỗi hãng theo đúng kiện và căn cứ tracking; phân tích số liệu kinh doanh S6, giữ phạm vi pilot HN/HCM và ghi quyết định v2 Tiếp tục sau khi cả bàn xác nhận report sau sửa.

### Bằng chứng

Tiêu chí được ký lúc `2026-11-18T15:03:46`, commit `a15fe63`, hash `5ad2d19d5cabaeced5eec3438761ef36541b41583c2eb5c3ecbccabae146afbf`. B8 v1 dùng `R-base-prepared-20261118-154614-a23b38` và `R-base-after-20261118-154443-b0af7a`; kết luận v1 là tiếp tục có điều kiện trong HN/HCM. Với S6, report cuối `R-S6-grade-20261118-170827-9e1216` so sánh base / prepared / after; after `R-S6-after-20261118-170827-9e1216` đạt `pass_rate=1,0`, `pass_k=1,0`, hoàn sai `0đ`, lỗi hãng oan `0`, PII `0`, ROI `0,45`, chi phí `6.887đ/ticket`, 0 ca ùn, escalation `0,25`, độ phủ `0,67`. Bộ nền sau sửa `R-base-after-20261118-170617-9e1216` không hồi quy, ROI `0,94`; tiêu chí ký và monitor đều đạt. C12 v2 được cả bàn chốt Tiếp tục trong HN/HCM, giữ 1 người trực và hẹn xem lại sau tuần đầu pilot / bài kiểm tra ẩn. Grade report vẫn ghi `FAIL` duy nhất ở integrity do repo này chỉ có gói sự cố S6 trong khi manifest kiểm tra các gói S1–S8; visible, regression và monitor đều đạt, và máy này không có test ẩn. Có sử dụng trợ lý AI để đọc repo, phân tích report và soạn specification; nhóm đã rà soát, cả bàn chịu trách nhiệm về quyết định cuối.

### Exit ticket

Học được rằng đặc tả đúng đơn vị dữ liệu (kiện thay vì đơn) và chuyển người khi thiếu căn cứ giúp loại bỏ các lỗi đã biết, nhưng có đánh đổi: S6 escalation tăng lên `0,25`, chi phí `6.887đ/ticket`, dù ROI vẫn `0,45` và độ phủ `0,67`. Cần kiểm chứng lại tracking cấp kiện, ROI, khiếu nại hãng nhỏ và hàng chờ trên dữ liệu pilot thật trước Bước đánh giá 2.


## NguyenMinhDat-2A202603582

### Phần việc phụ trách

Vai A – Kỹ sư cổng #1. Phụ trách `lab10/guards.py`, câu 2.6 (B7.1) của Phiếu B và các mục C6, C7, C9 của Phiếu C.

### Đóng góp cụ thể

- **Vòng 1:** Viết ba cổng để chặn ghi hoàn trùng, kiểm tra căn cứ ghi lỗi hãng và tính lại quyền lợi hoàn tiền từ tracking theo chính sách hiệu lực. Ghi mô tả và kết quả kiểm thử vào B7.1.
- **Vòng 2 – S6:** Sửa `write_gate` để ghi lỗi đúng kiện, hãng và tài xế theo tracking. Chuyển người duyệt trước khi hoàn tiền nếu nhiều kiện trễ mà ticket thiếu mã kiện, và chuyển duyệt khi hãng đã chạm trần ghi lỗi tự động trong ngày. Điền cây lỗi trước sửa, bảng biện pháp và cây lỗi sau sửa ở C6, C7, C9.
- **Sử dụng AI:** Dùng ChatGPT để đọc repo, hỗ trợ viết code cổng, cập nhật phiếu và giải thích kết quả. Tôi trực tiếp chạy các lệnh kiểm thử và đánh giá.

### Bằng chứng

- **Vòng 1:** Commit `a57d40a`. Qua 13 test công khai. Lần chạy `R-base-after-20261118-151055-60da30` đạt 65/65 lượt trong phạm vi pilot, với 0đ hoàn sai và 0 lỗi hãng oan.
- **Vòng 2:** Commit `1d7e5d3`. Qua 13 test công khai. Lần chạy S6 `R-S6-after-20261118-164735-172ce1` đạt 40/40 lượt trong phạm vi pilot, với 0đ hoàn sai và 0 lỗi hãng oan. Lần chạy hồi quy `R-base-after-20261118-164846-172ce1` đạt 65/65 lượt trong phạm vi pilot, không phát sinh ca hỏng.

### Exit ticket

Tôi học được rằng ticket thiếu mã kiện cần được chuyển duyệt trước khi ghi hoàn tiền. Tôi còn muốn kiểm tra cách hệ thống áp dụng trần ghi lỗi khi nhiều tiến trình cùng ghi cho một hãng.
