# Thực nghiệm thời gian chạy thuật toán Gale-Shapley (Bước A6 - NFR-01)

## 1. Mục tiêu kiểm chứng
- **Mã yêu cầu:** NFR-01
- **Chỉ tiêu:** Thời gian thực thi thuật toán ghép cặp ổn định cho 200 sinh viên đạt dưới 5 giây.

## 2. Kết quả đo thực nghiệm
Thực hiện đo bằng `time.perf_counter()` trung bình qua 5 seed ngẫu nhiên cho từng mốc quy mô dữ liệu:

| Quy mô mỗi nhóm (N) | Tổng số sinh viên (2N) | Thời gian chạy Gale-Shapley (giây) | Đánh giá NFR-01 (< 5s) |
| :---: | :---: | :---: | :---: |
| 50 | 100 | ~0.0005 s | Đạt |
| 100 | 200 | ~0.0018 s | Đạt (Vượt xa yêu cầu) |
| 200 | 400 | ~0.0075 s | Đạt |
| 500 | 1000 | ~0.0480 s | Đạt |

## 3. Nhận xét
Độ phức tạp lý thuyết của thuật toán Gale-Shapley là $O(N^2)$ nhờ sử dụng bảng tra cứu thứ hạng `rank_b` kiểu `dict` với thời gian truy xuất $O(1)$. Ở quy mô 200 sinh viên, thuật toán chỉ mất chưa đầy 2 mili-giây, hoàn toàn đáp ứng tiêu chí NFR-01.    