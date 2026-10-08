# Chương: Dữ liệu và công thức tương thích

## Mô hình dữ liệu

Mỗi sinh viên được biểu diễn bởi `Student`, gồm ID nội bộ, tên, nhóm A/B, giờ ngủ và thức dậy, mức gọn gàng, thói quen học, mức chịu ồn, hút thuốc, tần suất khách, sở thích và tiêu chí ưu tiên (`top`). CSV cần các cột `id`, `name`, `group`, `sleep`, `wake`, `tidy`, `study`, `noise`, `smoke`, `guests`, `hobbies`, `top`; nhiều sở thích được phân tách bằng dấu chấm phẩy.

ID nội bộ được gán theo thứ tự dòng sau khi nạp CSV để các ID luôn tương ứng với vị trí sinh viên trong ma trận điểm. Dữ liệu giả lập sử dụng bộ sinh số ngẫu nhiên riêng với `seed`, luân phiên nhóm A/B để cân bằng số lượng. Thuật toán tạo hai xu hướng giờ ngủ: nhóm ngủ sớm tập trung quanh 22 giờ và nhóm cú đêm quanh 25 giờ.

## Tiêu chí tương thích

Mỗi tiêu chí tạo độ giống trong đoạn [0, 1]. Các tiêu chí số dùng công thức `max(0, min(1, 1 - |x - y| / d))`, trong đó `d` là khoảng chuẩn hóa của thuộc tính.

| Tiêu chí | Trọng số | Cách tính độ giống |
|---|---:|---|
| Giờ đi ngủ | 0.25 | Chuẩn hóa chênh lệch, `d = 5` |
| Giờ thức dậy | 0.10 | Chuẩn hóa chênh lệch, `d = 5` |
| Gọn gàng | 0.20 | Chuẩn hóa chênh lệch, `d = 4` |
| Thói quen học | 0.10 | 1 nếu cùng lựa chọn, ngược lại 0 |
| Chịu ồn | 0.15 | Chuẩn hóa chênh lệch, `d = 4` |
| Hút thuốc | 0.10 | 1 nếu cùng lựa chọn, ngược lại 0 |
| Khách đến phòng | 0.05 | Chuẩn hóa chênh lệch, `d = 4` |
| Sở thích | 0.05 | Jaccard: số sở thích chung chia cho số sở thích hợp |

Trọng số ưu tiên các thói quen ảnh hưởng trực tiếp đến sinh hoạt chung như giờ ngủ, gọn gàng và tiếng ồn. Các lựa chọn trùng khớp (học, hút thuốc) và sở thích có trọng số thấp hơn vì mức ảnh hưởng đến khả năng ở chung thường phụ thuộc từng cá nhân. Tổng trọng số cơ sở bằng 1.

## Công thức điểm

Với sinh viên `x`, tiêu chí ưu tiên `top` của người đó được nhân trọng số 1.5; sau đó chuẩn hóa theo tổng trọng số mới:

`Score(x, y) = 100 * sum(w'_k * similarity_k(x, y)) / sum(w'_k)`

Điểm nằm trong [0, 100]. Vì `top` thuộc về người đánh giá, `Score(x, y)` có thể khác `Score(y, x)`. Ma trận `M[i][j]` lưu điểm từ sinh viên thứ `i` đánh giá sinh viên thứ `j`; đường chéo chính bằng 0. Danh sách ưu tiên của mỗi người được sắp giảm dần theo điểm đánh giá dành cho thành viên nhóm đối diện.

## Kiểm thử

`tests/test_scoring.py` kiểm tra điểm 100 cho hai hồ sơ giống nhau, điểm hai chiều bất đối xứng, miền điểm, ma trận và thứ tự ưu tiên của cả hai nhóm. `tests/test_data_io.py` kiểm tra CSV mẫu 20 sinh viên, chuẩn hóa ID, CSV thiếu cột, dữ liệu số không hợp lệ, file rỗng, nhóm lệch số lượng và tính tái lập của dữ liệu giả lập.

Chạy `python -m pytest -q`: **10 test đạt**. Các trường hợp CSV lỗi được báo thành ngoại lệ ở lớp nạp dữ liệu; tab dữ liệu bắt ngoại lệ và hiển thị thông báo lỗi thay vì làm dừng ứng dụng.