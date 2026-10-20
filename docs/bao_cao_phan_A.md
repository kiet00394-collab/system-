# BÁO CÁO TỔNG HỢP PHẦN CỦA NGƯỜI A (BƯỚC A7 - TUẦN 6)

## 1. Cơ sở lý thuyết và Mô hình hóa bài toán
- **Mô hình cốt lõi:** Dựa trên bài toán Hôn nhân Ổn định (*Stable Marriage Problem*) được giới thiệu bởi Gale & Shapley (1962).
- **Giả định hai phía (Bipartite):** Chia tập hợp sinh viên thành Nhóm A (bên chủ động đề nghị) và Nhóm B (bên xét duyệt) có kích thước bằng nhau.
- **Cặp chặn (*Blocking Pair*) và Tính ổn định:** Định nghĩa cụ thể về cặp chặn và điều kiện để một phép ghép đạt độ ổn định tuyệt đối (số cặp chặn bằng 0).

## 2. Mã giả và Độ phức tạp thuật toán
- Sử dụng bảng băm tra cứu thứ hạng ưu tiên (`rank_b`) giúp các thao tác kiểm tra, so sánh đạt độ phức tạp $\mathcal{O}(1)$.
- **Độ phức tạp tổng thể:** Thời gian $\mathcal{O}(N^2)$ và không gian $\mathcal{O}(N^2)$.

## 3. Chứng minh tính đúng đắn toán học
- **Tính dừng:** Chứng minh thuật toán chắc chắn kết thúc sau tối đa $N^2$ lượt đề nghị do mỗi sinh viên nhóm A không lặp lại việc đề nghị cùng một đối tượng.
- **Tính ổn định:** Chứng minh không tồn tại bất kỳ cặp chặn nào trong kết quả trả về.
- **Tính tối ưu (A-optimal):** Đảm bảo mang lại kết quả tốt nhất cho sinh viên bên phía nhóm A trong mọi phép ghép ổn định.

## 4. Mở rộng thuật toán gộp phòng 4 người (`merge_pairs_into_rooms`)
- Trình bày phương pháp tính điểm tương thích chéo trung bình giữa các cặp đôi để ghép nối tham lam thành các phòng 4 người có mức độ hòa hợp cao nhất.

## 5. Phân tích hạn chế và Hướng mở rộng
- **Hạn chế:** Mô hình hai phía không hỗ trợ trường hợp sinh viên tự do ghép đôi mà không phân biệt nhóm.
- **So sánh mở rộng:** Đối chiếu với bài toán *Stable Roommates* và **Thuật toán Irving (1985)** khi không phân chia nhóm, đồng thời phân tích các trường hợp có thể vô nghiệm (*odd-length cycles*).

## 6. Tổng hợp kết quả Kiểm thử và Thực nghiệm
- **Kiểm thử tự động (NFR-02, NFR-06):** Hoàn thành vượt mức qua 50 seed kiểm thử ngẫu nhiên với kết quả số cặp chặn luôn bằng 0.
- **Thực nghiệm hiệu năng (NFR-01):** Tổng hợp bảng số liệu thời gian chạy thực tế từ quy mô 100, 200, 400 đến 1000 sinh viên (ví dụ: 200 sinh viên xử lý trong $\sim0.0018$ giây, vượt chuẩn yêu cầu dưới 5 giây).