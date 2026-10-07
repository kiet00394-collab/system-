# Bảng yêu cầu phi chức năng (NFR) - Nhóm Ghép phòng KTX

| Mã | Tên yêu cầu | Nội dung chi tiết | Cách kiểm chứng |
|---|---|---|---|
| NFR-01 | Hiệu năng thời gian | Thời gian thực thi thuật toán ghép cặp < 5 giây đối với quy mô 200 sinh viên. | Đo bằng module `time.perf_counter()` khi chạy thực nghiệm. |
| NFR-02 | Tính ổn định | Kết quả ghép cặp không tồn tại cặp chặn (blocking pair), số cặp chặn = 0. | Kiểm tra bằng hàm `count_blocking_pairs()` trên 50 seed ngẫu nhiên. |
| NFR-06 | Kiểm thử tự động | Toàn bộ các module cốt lõi phải có Unit Test độc lập. | Chạy lệnh `pytest -v` vượt qua 100% test case. |
| NFR-08 | Tái lập kết quả | Thuật toán và dữ liệu phải cho kết quả đồng nhất khi dùng cùng một seed ngẫu nhiên. | Cố định giá trị `seed` đầu vào để kiểm tra tính nhất quán. |