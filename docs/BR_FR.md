# Yêu cầu Nghiệp vụ (BR) và Yêu cầu Chức năng (FR)

## 1. Yêu cầu Nghiệp vụ (Business Requirements - BR)

| Mã BR | Nội dung yêu cầu | Chỉ tiêu đo lường / Mục tiêu |
| :--- | :--- | :--- |
| **BR-01** | Giảm thiểu tối đa xung đột cá nhân giữa các sinh viên cùng phòng KTX | Điểm hài lòng trung bình tăng $\ge 20\%$ so với phương pháp phân phòng ngẫu nhiên |
| **BR-02** | Đảm bảo tính ổn định trong việc xếp phòng, không sinh viên nào muốn tự ý đổi phòng | Số cặp chặn (blocking pairs) bằng $0$ |
| **BR-03** | Tối ưu hóa quy trình phân phòng cho Ban quản lý KTX | Thời gian xử lý ghép phòng $\le 5$ giây cho quy mô 200 sinh viên |
| **BR-04** | Minh bạch hóa lý do ghép phòng cho sinh viên | Cung cấp thông tin giải thích chi tiết các tiêu chí phù hợp cho từng cặp phòng |

---

## 2. Yêu cầu Chức năng (Functional Requirements - FR)

| Mã FR | Chức năng | Mô tả chi tiết | Độ ưu tiên | Người phụ trách | Mã SR liên quan |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **FR-01** | Nhập dữ liệu thủ công | Cho phép người dùng nhập thông tin 1 sinh viên mới qua biểu mẫu form | Trung bình | Người B | SR-01 |
| **FR-02** | Nạp dữ liệu từ file CSV | Tải lên và parse danh sách sinh viên từ file CSV | Cao | Người B | SR-02 |
| **FR-03** | Sinh dữ liệu giả lập | Sinh tự động $N$ sinh viên giả lập dựa trên tham số `seed` và số lượng $N$ | Cao | Người B | SR-03 |
| **FR-04** | Tính ma trận tương thích | Tính toán ma trận điểm $M[i][j]$ dựa trên 8 tiêu chí thói quen | Cao | Người B | SR-04 |
| **FR-05** | Lập danh sách ưu tiên | Chuyển ma trận điểm thành danh sách ưu tiên 2 phía `pref_a` và `pref_b` | Cao | Người B | SR-04 |
| **FR-06** | Thuật toán Gale-Shapley | Thực hiện ghép cặp ổn định giữa nhóm A và nhóm B | Cao | Người A | SR-05 |
| **FR-07** | Ghép phòng ngẫu nhiên | Thực hiện ghép phòng ngẫu nhiên để làm cơ sở đối chứng | Cao | Người A | SR-05 |
| **FR-08** | Đếm số cặp chặn | Đếm số cặp chặn (blocking pairs) để đánh giá độ ổn định | Cao | Người A | SR-06 |
| **FR-09** | Giải thích cặp ghép | Phân tích các tiêu chí trùng khớp và cần lưu ý của từng phòng | Cao | Người C | SR-07 |
| **FR-10** | Đánh giá & So sánh | Tính điểm hài lòng TB và vẽ biểu đồ so sánh Gale-Shapley vs Ngẫu nhiên | Cao | Người C | SR-07 |
| **FR-11** | Xuất kết quả | Tải về kết quả phân phòng dưới dạng file CSV | Trung bình | Người C | SR-08 |
