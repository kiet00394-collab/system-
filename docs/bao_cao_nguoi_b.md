# BÁO CÁO CHI TIẾT PHẦN VIỆC NGƯỜI B: DỮ LIỆU VÀ CÔNG THỨC ĐIỂM TƯƠNG THÍCH

**Sinh viên thực hiện:** Châu Tuấn Kiệt (Người B)  
**Học phần:** Đồ án cơ sở / Hệ thống ghép phòng KTX  

---

## 1. TỔNG QUAN VAI TRÒ VÀ TRÁCH NHIỆM

Người B chịu trách nhiệm thiết kế toàn bộ nền tảng dữ liệu và thuật toán đánh giá độ tương thích giữa các sinh viên, bao gồm:
* Khai báo mô hình dữ liệu sinh viên (`models.py`).
* Xây dựng bộ nạp file CSV và sinh dữ liệu giả lập (`data_io.py`).
* Thiết lập bộ 8 tiêu chí sinh hoạt và công thức tính điểm tương thích hai chiều (`scoring.py`).
* Xây dựng giao diện Tab 1 "Dữ liệu" trên Streamlit (`ui/tab_data.py`).
* Viết tài liệu yêu cầu nghiệp vụ và chức năng (`docs/BR_FR.md`).

---

## 2. HỆ THỐNG 8 TIÊU CHÍ SINH HOẠT VÀ BỘ TRỌNG SỐ

Để mô hình hóa chính xác mức độ hòa hợp giữa hai người sống chung phòng, hệ thống sử dụng 8 tiêu chí:

| Tiêu chí | Trọng số (`WEIGHTS`) | Miền giá trị | Công thức độ giống ($\text{sim} \in [0, 1]$) | Ý nghĩa thực tiễn |
| :--- | :---: | :---: | :--- | :--- |
| **Giờ đi ngủ (`sleep`)** | **25%** | $21.0 - 26.0$ | $\max(0, 1 - \|x.sleep - y.sleep\| / 5)$ | Nguyên nhân hàng đầu gây mất ngủ và căng thẳng |
| **Mức gọn gàng (`tidy`)** | **20%** | $1 - 5$ | $1 - \|x.tidy - y.tidy\| / 4$ | Tranh cãi phổ biến về vệ sinh không gian chung |
| **Mức chịu ồn (`noise`)** | **15%** | $1 - 5$ | $1 - \|x.noise - y.noise\| / 4$ | Ảnh hưởng đến việc nghỉ ngơi và tập trung |
| **Giờ thức dậy (`wake`)** | **10%** | $5.0 - 10.0$ | $\max(0, 1 - \|x.wake - y.wake\| / 5)$ | Tránh làm phiền người khác khi thức giấc sớm |
| **Thói quen học (`study`)** | **10%** | `phong`, `thuvien`, `it` | $1.0$ nếu giống nhau, $0.0$ nếu khác | Đảm bảo môi trường học tập yên tĩnh tại phòng |
| **Hút thuốc (`smoke`)** | **10%** | $0$ (Không), $1$ (Có) | $1.0$ nếu giống nhau, $0.0$ nếu khác | Tiêu chí sức khỏe và mùi phòng cực kỳ nhạy cảm |
| **Hay có khách (`guests`)** | **5%** | $1 - 5$ | $1 - \|x.guests - y.guests\| / 4$ | Mức độ riêng tư trong sinh hoạt cá nhân |
| **Sở thích chung (`hobbies`)** | **5%** | Tập hợp chuỗi | $\frac{\|x.hobbies \cap y.hobbies\|}{\|x.hobbies \cup y.hobbies\|}$ (Jaccard) | Tạo sự gắn kết và giao lưu vui vẻ trong phòng |

---

## 3. CÔNG THỨC TÍNH ĐIỂM TƯƠNG THÍCH BẤT ĐỐI XỨNG (`pair_score`)

Điểm số mà sinh viên $x$ đánh giá sinh viên $y$ được tính theo công thức:

$$\text{Score}(x, y) = 100 \times \frac{\sum_{k} w_k \cdot \text{sim}_k(x, y)}{\sum_k w_k}$$

Trong đó:
* Nếu tiêu chí $k = x.top$ (tiêu chí mà $x$ coi trọng nhất), trọng số của tiêu chí đó được nhân thêm hệ số **$1.5$**:
  $$w_{x.top} = \text{WEIGHTS}[x.top] \times 1.5$$
* **Tính chất bất đối xứng cốt lõi ($M[x][y] \neq M[y][x]$)**:
  Do mỗi sinh viên có tiêu chí ưu tiên $top$ khác nhau, người $x$ có thể thấy rất hợp với $y$, nhưng người $y$ lại thấy người $x$ không đáp ứng kỳ vọng quan trọng nhất của mình. Điều này phản ánh hoàn hảo tâm lý thực tế và tạo tiền đề để thuật toán Gale-Shapley (hai phía) phát huy tác dụng.

---

## 4. CƠ CHẾ SINH DỮ LIỆU GIẢ LẬP ĐA PHÂN PHỐI (`generate_students`)

Dữ liệu giả lập không sinh ngẫu nhiên hoàn toàn mà mô phỏng theo hành vi thực tế của sinh viên KTX:
* **Tạo 2 cụm sinh học rõ rệt**:
  - Nhóm "Cú đêm" (tỷ lệ 40%): Giờ đi ngủ trung bình khoảng 1h sáng ($25.0$), phân phối chuẩn $\mathcal{N}(25, 0.8^2)$.
  - Nhóm "Ngủ sớm" (tỷ lệ 60%): Giờ đi ngủ trung bình khoảng 22h đêm ($22.0$), phân phối chuẩn $\mathcal{N}(22, 0.8^2)$.
* **Tương quan sinh học**: Giờ thức dậy được sinh phụ thuộc vào giờ đi ngủ $\text{wake} \approx \text{sleep} - 15 + \mathcal{N}(0, 0.7^2)$ (đảm bảo ngủ đủ 7-8 tiếng).
* **Phân bổ đều hai phía**: Sử dụng `i % 2 == 0` để chia chính xác $50\%$ sinh viên thuộc nhóm A và $50\%$ thuộc nhóm B.
* **Tái lập kết quả (Reproducibility)**: Cố định bằng tham số `seed`, giúp việc kiểm thử và chạy thực nghiệm đối chứng luôn đồng nhất.

---

## 5. KẾT QUẢ KIỂM THỬ XỬ LÝ DỮ LIỆU LỖI (NFR-04)

Để đảm bảo hệ thống không bị crash khi người dùng tải lên file CSV không chuẩn, nhóm B đã xây dựng bộ kiểm thử tự động với các kịch bản lỗi:
1. **Thiếu cột bắt buộc (`error_missing_cols.csv`)**: Bắt lỗi và thông báo chính xác danh sách các cột bị thiếu.
2. **Sai định dạng kiểu dữ liệu (`error_invalid_types.csv`)**: Báo lỗi cụ thể dòng và tên trường (ví dụ: dòng 2 trường `sleep` phải là số thực).
3. **File rỗng (`error_empty.csv`)**: Báo lỗi file không chứa dữ liệu sinh viên.
4. **Lệch sĩ số giữa hai nhóm A và B**: Hệ thống vẫn tính toán ma trận điểm bình thường; người thừa ở nhóm nhiều hơn sẽ hiển thị chưa ghép phòng.
