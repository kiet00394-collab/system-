# MA TRẬN TRUY VẾT YÊU CẦU (REQUIREMENTS TRACEABILITY MATRIX)

**Phụ trách quản lý & truy vết:** Hoàng Triều (Người C - Quản lý Repo & Đánh giá)  
**Phối hợp đóng góp:** Bùi Đình Hiếu (Người A), Châu Tuấn Kiệt (Người B)  

---

## BẢNG TRUY VẾT LIÊN HOÀN: BR ↔ SR ↔ FR ↔ TEST / KẾT QUẢ

| Mã BR | Yêu cầu Nghiệp vụ (BR) | Mã SR | Yêu cầu Bên liên quan (SR) | Mã FR | Yêu cầu Chức năng (FR) | File cài đặt / Test case kiểm chứng |
| :---: | :--- | :---: | :--- | :---: | :--- | :--- |
| **BR-01** | Giảm xung đột phòng, điểm hài lòng tăng $\ge 20\%$ so với ngẫu nhiên | **SR-01** | SV khai báo khảo sát 8 tiêu chí và tiêu chí `top` | **FR-01**<br>**FR-04** | Form nhập tay sinh viên;<br>Tính điểm tương thích `pair_score` | `ui/tab_data.py`<br>`scoring.py`<br>`tests/test_scoring.py` |
| **BR-01** | Minh bạch hóa lý do ghép phòng cho sinh viên | **SR-02**<br>**SR-03** | SV xem bạn ghép, điểm 2 chiều và danh sách tiêu chí trùng/lưu ý | **FR-09** | Giải thích cặp ghép `explain_pair` | `explain.py`<br>`ui/tab_explain.py` |
| **BR-02** | Xếp phòng ổn định tuyệt đối (0 cặp chặn) | **SR-05** | Ban QL chạy thuật toán ghép ổn định hai phía | **FR-06**<br>**FR-08** | Thuật toán `gale_shapley`;<br>Đếm số cặp chặn `count_blocking_pairs` | `matching.py`<br>`tests/test_matching.py` (50 seed xanh) |
| **BR-03** | Tối ưu hóa quy trình phân phòng cho BQL KTX | **SR-04** | Nạp CSV khảo sát hoặc sinh dữ liệu giả lập có `seed` | **FR-02**<br>**FR-03** | Đọc file CSV `load_students_csv`;<br>Sinh dữ liệu `generate_students` | `data_io.py`<br>`tests/test_data_io.py`<br>`tests/test_perf_scoring.py` (< 1s) |
| **BR-03** | Báo cáo đánh giá và xuất kết quả | **SR-06**<br>**SR-08** | BQL xem biểu đồ đối chứng và tải file kết quả | **FR-10**<br>**FR-11** | Chạy thực nghiệm `run_experiment`;<br>Tải CSV phân phòng | `evaluation.py`<br>`ui/tab_compare.py`<br>`ui/tab_match.py` |
| **BR-04** | Minh bạch và kiểm thử toàn diện hệ thống | **SR-07** | Giảng viên theo dõi kiểm thử unit test và quy trình PR | - | Kiểm thử tự động `pytest -v`;<br>Quy trình Git feature branch & PR | `tests/`<br>GitHub Pull Requests |
