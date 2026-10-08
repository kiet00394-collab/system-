# TÀI LIỆU YÊU CẦU BÊN LIÊN QUAN (SR) VÀ YÊU CẦU THÔNG TIN (IR)
**Dự án:** Hệ thống ghép phòng KTX tự động dựa trên thuật toán Gale-Shapley
**Phân công:** Người C (Giao diện, Đánh giá thực nghiệm & Quản lý Repo)

---

## I. YÊU CẦU BÊN LIÊN QUAN (STAKEHOLDER REQUIREMENTS - SR)

| Mã SR | Bên liên quan (Stakeholder) | Nhu cầu / Yêu cầu chi tiết | Mã BR liên quan |
| :--- | :--- | :--- | :--- |
| **SR-01** | **Sinh viên** | Khai báo các thông tin khảo sát 8 tiêu chí sinh hoạt (giờ ngủ, thức dậy, gọn gàng, học tập, độ ồn, hút thuốc, khách, sở thích) và tiêu chí ưu tiên nhất (`top`). | BR-01 |
| **SR-02** | **Sinh viên** | Tra cứu/Xem kết quả phân phòng cùng danh tính bạn ở ghép và điểm đánh giá tương thích 2 chiều (\\(M[a][b]\\) và \\(M[b][a]\\)). | BR-01 |
| **SR-03** | **Sinh viên** | Xem lời giải thích minh bạch về lý do được ghép chung (danh sách tiêu chí trùng khớp \\(\ge 0.8\\) và các tiêu chí cần lưu ý \\(\le 0.4\\)). | BR-01 |
| **SR-04** | **Ban quản lý KTX** | Nạp dữ liệu danh sách sinh viên dễ dàng từ file CSV khảo sát hoặc tự sinh dữ liệu giả lập có `seed` để thử nghiệm quy mô. | BR-02 |
| **SR-05** | **Ban quản lý KTX** | Thực hiện ghép phòng tự động đảm bảo tính ổn định cao (0 cặp chặn - không có 2 sinh viên nào muốn bỏ phòng hiện tại để ghép với nhau). | BR-02 |
| **SR-06** | **Ban quản lý KTX** | Xem báo cáo đánh giá thực nghiệm và biểu đồ cột so sánh điểm hài lòng trung bình giữa thuật toán Gale-Shapley và ghép ngẫu nhiên trên các quy mô \\(N \in \{20, 50, 100, 200\}\\). | BR-03 |
| **SR-07** | **Giảng viên** | Đánh giá tính đúng đắn của thuật toán, kiểm thử unit test (`pytest`), bảng truy vết yêu cầu và theo dõi tiến độ dự án qua Pull Request trên GitHub. | BR-04 |

---

## II. YÊU CẦU THÔNG TIN (INFORMATION REQUIREMENTS - IR)

### 1. Dữ liệu Đầu vào (Input Requirements - IR-IN)
Dữ liệu được nạp từ file CSV khảo sát (`data/sample_students.csv`) hoặc sinh tự động qua hàm `generate_students(n, seed)`:

| Trường dữ liệu | Kiểu dữ liệu | Mô tả & Miền giá trị |
| :--- | :--- | :--- |
| `id` | Integer | Mã định danh duy nhất của sinh viên (`0, 1, 2...`). |
| `name` | String | Họ và tên sinh viên (`SV000`, `SV001`...). |
| `group` | String | Phân nhóm hai phía: `"A"` (sinh viên cũ) hoặc `"B"` (sinh viên mới). |
| `sleep` | Float | Giờ đi ngủ (giá trị từ `21` đến `26`, trong đó `26` tương ứng 2h sáng). |
| `wake` | Float | Giờ thức dậy (giá trị từ `5` đến `10`). |
| `tidy` | Integer | Mức độ sạch sẽ, ngăn nắp (thang điểm `1` đến `5`). |
| `study` | String | Thói quen học tập (`"phong"`, `"thuvien"`, `"it"`). |
| `noise` | Integer | Mức độ tiếng ồn chấp nhận (thang điểm `1` đến `5`). |
| `smoke` | Integer | Tình trạng hút thuốc (`0`: Không, `1`: Có). |
| `guests` | Integer | Mức độ hay dắt bạn về phòng (thang điểm `1` đến `5`). |
| `hobbies` | String/Set | Danh sách sở thích, phân tách bởi dấu `;` (ví dụ: `game;nhac;the thao`). |
| `top` | String | Tiêu chí quan trọng nhất cá nhân (`sleep`, `tidy`, `noise`, `study`, `smoke`...). |

### 2. Dữ liệu Trung gian & Xử lý (Intermediate Processing - IR-PROC)
* **Ma trận điểm tương thích \\(M\\)**: Ma trận kích thước \\(N \times N\\), trong đó \\(M[i][j]\\) là điểm số (\\(0 - 100\\)) mà sinh viên \\(i\\) đánh giá độ phù hợp của sinh viên \\(j\\).
* **Danh sách ưu tiên (`pref_a`, `pref_b`)**: 
  * `pref_a`: Dictionary lưu danh sách ID sinh viên nhóm B xếp theo thứ tự điểm giảm dần từ góc nhìn nhóm A.
  * `pref_b`: Dictionary lưu danh sách ID sinh viên nhóm A xếp theo thứ tự điểm giảm dần từ góc nhìn nhóm B.

### 3. Dữ liệu Đầu ra (Output Requirements - IR-OUT)
* **Kết quả ghép cặp (`match`)**: Dictionary dạng `{id_A: id_B}` thể hiện các cặp sinh viên xếp chung phòng.
* **Điểm hài lòng 2 chiều**: Chỉ số \\(M[a][b]\\) và \\(M[b][a]\\) hiển thị cho từng phòng.
* **Chuỗi giải thích tương thích**: Văn bản tự động từ hàm `explain_pair(x, y)` liệt kê tiêu chí *"Trùng khớp"* (\\(\ge 0.8\\)) và *"Cần lưu ý"* (\\(\le 0.4\\)).
* **Dữ liệu so sánh thực nghiệm**: Biểu đồ cột thể hiện điểm hài lòng trung bình giữa Gale-Shapley và Ghép ngẫu nhiên.
* **File xuất kết quả (CSV)**: Cho phép Ban quản lý KTX tải về file CSV danh sách phân phòng hoàn chỉnh.