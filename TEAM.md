# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng):Ubuntu
- Lớp: `L3A` 
- Repo của bàn: cuongdc03/K5-L3A-DAY10-Ubuntu-PoCtoPilotGate1
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên    | MSSV        | Vai | Trưởng nhóm |
| --: | ------------ | ----------- | --- | :---------: |
| 1   | Đỗ Cao Cường | 2A202603612 | D   | x           |
| 2   | Kiệt         |             | B   |             |
| 3   | Trịnh Công Đức| 2A202603527| C   |             |
| 4   | Nguyễn Minh Đạt | 2A202603582 | A   |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Phân công chi tiết (4 người)

Điền tên vào cột "Người" rồi chép vai sang cột "Vai" của bảng thành viên. Quyết định v1 và v2 do **cả bàn** chốt.

| Mã  | Vai                                   | Người        | File / phiếu chính                                                                          |
| --- | ------------------------------------- | ------------ | ------------------------------------------------------------------------------------------- |
| A   | Kỹ sư cổng #1 (viết code)             | Đạt          | `lab10/guards.py` (`pre_guard`, `write_gate`)                                               |
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

## TrinhCongDuc-2A202603527

### Phần việc phụ trách

Vai C — Sản phẩm và kinh doanh: Phiếu A câu 1.1, 1.6; Phiếu B câu 2.3, 2.9; Phiếu C câu 3.2, phần kinh doanh của sự cố và C12; `config/acceptance_criteria.json` và mục `business` trong `config/operating_gates.json`.

### Đóng góp cụ thể

Soạn mục tiêu hệ thống, đề xuất tiêu chí chấp nhận và quy tắc quyết định; lập bản đồ dữ liệu/trường nguồn sự thật, nêu ví dụ drift chính sách; đề xuất trần chi phí, ROI, ngân sách hoàn và phạm vi pilot dựa trên `data/world.json`. Các ngưỡng và phạm vi hiện là bản dự thảo để cả bàn rà soát trước khi ký.

### Bằng chứng

Các phần đã điền ở Phiếu A, Phiếu B và hai config; chưa có mã lần chạy vì tiêu chí chưa ký và chưa chạy eval. Có sử dụng trợ lý AI để đọc repo, soạn bản nháp và giải thích cách làm; nhóm cần tự rà soát, thống nhất và chịu trách nhiệm về quyết định cuối.

### Exit ticket

Học được rằng phải chốt tiêu chí trước khi đo, và mỗi ngưỡng kinh doanh cần gắn với một hành động/quyết định. Còn cần kiểm chứng trong report liệu phạm vi HN/HCM, tỷ lệ chuyển người và ROI có khả thi khi tính cả chi phí vận hành hay không.


## NguyenMinhDat-2A202603582

### Phần việc phụ trách

Vai A – Kỹ sư cổng #1. Phụ trách câu 2.6, mục B7.1 của Phiếu B và các mục C6, C7, C9 của Phiếu C.

### Đóng góp cụ thể

Ở vòng 1, viết ba cổng trong `lab10/guards.py`: chặn ghi hoàn trùng, kiểm tra căn cứ ghi lỗi hãng và tính lại quyền lợi hoàn tiền theo tracking và chính sách hiệu lực. Cập nhật mô tả và kết quả kiểm thử ở B7.1.

### Bằng chứng

- Commit `a57d40a` trên nhánh `dat/vai-a-vong-1`.
- 13 test công khai đạt.
- Lần chạy `R-base-after-20261118-151055-60da30` đạt 65/65 lượt trong phạm vi pilot, với 0đ hoàn sai và 0 lỗi hãng oan.

### Exit ticket

Tôi học được cách kiểm tra quyền lợi từ tracking và chính sách trước khi ghi hoàn tiền. Tôi còn muốn kiểm tra cổng sẽ xử lý thế nào khi chính dữ liệu tracking bị thiếu hoặc cập nhật trễ.
