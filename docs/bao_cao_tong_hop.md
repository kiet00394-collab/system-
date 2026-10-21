# BÁO CÁO TỔNG HỢP TOÀN DIỆN ĐỒ ÁN
# HỆ THỐNG GHÉP PHÒNG KÝ TÚC XÁ TỰ ĐỘNG (GALE-SHAPLEY DORM MATCHING)

**Học phần:** System Engineering / Đồ án Kỹ thuật Hệ thống  
**Nhóm sinh viên thực hiện:**
1. **Bùi Đình Hiếu** (Người A) - Phụ trách Thuật toán ghép cặp & Tối ưu (`matching.py`, Tab 2)
2. **Châu Tuấn Kiệt** (Người B) - Phụ trách Mô hình dữ liệu & Công thức tính điểm tương thích (`models.py`, `data_io.py`, `scoring.py`, Tab 1)
3. **Lê Hoàng Triệu** (Người C) - Phụ trách Module Giải thích & Đánh giá mô phỏng (`explain.py`, `evaluation.py`, Tab 3, Tab 4, Quản trị Repo)

---

## MỤC LỤC
1. [Giới thiệu Đề tài và Động lực Nghiên cứu](#1-giới-thiệu-đề-tài-và-động-lực-nghiên-cứu)
2. [Kiến trúc Hệ thống và Phân công Module](#2-kiến-trúc-hệ-thống-và-phân-công-module)
3. [Phần việc Người B: Dữ liệu và Công thức Điểm tương thích](#3-phần-việc-người-b-dữ-liệu-và-công-thức-điểm-tương-thích)
4. [Phần việc Người A: Thuật toán Gale-Shapley và Phân tích](#4-phần-việc-người-a-thuật-toán-gale-shapley-và-phân-tích)
5. [Phần việc Người C: Giải thích Cặp ghép và Thực nghiệm Đối chứng](#5-phần-việc-người-c-giải-thích-cặp-ghép-và-thực-nghiệm-đối-chứng)
6. [Phân tích Hạn chế Mô hình Hai phía và So sánh Thuật toán Stable Roommates](#6-phân-tích-hạn-chế-mô-hình-hai-phía-và-so-sánh-thuật-toán-stable-roommates)
7. [Ma trận Truy vết và Kết quả Kiểm thử Toàn diện](#7-ma-trận-truy-vết-và-kết-quả-kiểm-thử-toàn-diện)
8. [Kết luận và Hướng phát triển](#8-kết-luận-và-hướng-phát-triển)

---

## 1. Giới thiệu Đề tài và Động lực Nghiên cứu

Trong môi trường ký túc xá đại học, việc sắp xếp phòng ở truyền thống (theo thứ tự nộp đơn hoặc phân bổ ngẫu nhiên) thường tạo ra những tập hợp sinh viên có thói quen sinh hoạt xung khắc gay gắt:
- Cú đêm (thức tới 2h sáng) sống chung phòng với người dậy sớm (5h sáng).
- Người yêu cầu sự yên tĩnh tuyệt đối sống chung với người thích nghe nhạc, trò chuyện ồn ào.
- Người ưa sạch sẽ, ngăn nắp sống chung với người bừa bộn.
- Vấn đề mùi thuốc lá và dắt bạn bè về phòng riêng.

Những xung đột này ảnh hưởng tiêu cực trực tiếp đến sức khỏe tâm lý, kết quả học tập và gây áp lực lớn cho Ban Quản lý KTX trong việc xử lý đơn xin chuyển phòng.

**Mục tiêu của dự án:**  
Xây dựng một hệ thống phần mềm hoàn chỉnh, tự động hóa quá trình ghép phòng dựa trên cơ sở khoa học:
1. Thu thập dữ liệu khảo sát 8 tiêu chí sinh hoạt cốt lõi.
2. Xây dựng hàm khoảng cách/tương thích có trọng số cá nhân hóa nhằm tạo ra danh sách ưu tiên hai chiều bất đối xứng.
3. Ứng dụng giải thuật **Gale-Shapley (Deferred Acceptance Algorithm)** để bảo đảm triệt tiêu hoàn toàn các cặp chặn (**Blocking Pairs = 0**), đem lại sự ổn định toán học tuyệt đối.
4. Cung cấp giao diện tương tác trực quan (Streamlit) với khả năng giải thích lý do ghép cặp, mô phỏng đối chứng hiệu năng với giải pháp ghép ngẫu nhiên và xuất báo cáo CSV.

---

## 2. Kiến trúc Hệ thống và Phân công Module

Hệ thống được thiết kế theo mô hình phân lớp rõ ràng, đảm bảo tính mô-đun hóa cao:

```
[ Dữ liệu CSV / Giả lập ] (B: data_io.py)
            │
            ▼
[ Danh sách sinh viên (Student) ] (B: models.py)
            │
            ▼
[ Ma trận điểm tương thích 2 chiều M[x][y] ] (B: scoring.py)
            │
            ▼
[ Danh sách thứ tự ưu tiên pref_a, pref_b ] (B: scoring.py)
            │
            ▼
[ Thuật toán Gale-Shapley ] (A: matching.py) ──► [ Đếm cặp chặn & Gộp phòng 4 ]
            │
            ├─────────────────────────────────────────┐
            ▼                                         ▼
[ Giải thích tiêu chí (C: explain.py) ]    [ Đánh giá & So sánh (C: evaluation.py) ]
            │                                         │
            ▼                                         ▼
[ Giao diện Tab 3: Giải thích ]            [ Giao diện Tab 4: So sánh thực nghiệm ]
```

### Phân công trách nhiệm:
* **Người B (Châu Tuấn Kiệt):** Phụ trách tầng dữ liệu và công thức điểm:
  - `models.py`: Khai báo kiểu thực thể `Student`.
  - `data_io.py`: Đọc/ghi CSV, kiểm tra tính toàn vẹn dữ liệu (NFR-04), sinh dữ liệu giả lập có phân cụm.
  - `scoring.py`: Tính điểm tương thích hai chiều `pair_score`, ma trận điểm $M$, xây dựng danh sách ưu tiên `pref_a`, `pref_b`.
  - `ui/tab_data.py`: Giao diện Tab 1 nạp dữ liệu.
* **Người A (Bùi Đình Hiếu):** Phụ trách tầng thuật toán ghép cặp:
  - `matching.py`: Thuật toán `gale_shapley`, `count_blocking_pairs`, `merge_pairs_into_rooms`, `run_benchmark`, `analyze_matching_quality`.
  - `ui/tab_match.py`: Giao diện Tab 2 thực hiện phân phòng và đo hiệu năng NFR-01.
* **Người C (Lê Hoàng Triệu):** Phụ trách tầng giải thích, đánh giá và quản trị repo:
  - `explain.py`: Giải thích tiêu chí hòa hợp ($\ge 0.8$) và lưu ý ($\le 0.4$).
  - `evaluation.py`: Tính điểm thỏa mãn trung bình `avg_satisfaction` và chạy mô phỏng đối chứng `run_experiment`.
  - `ui/tab_explain.py`, `ui/tab_compare.py`: Giao diện Tab 3 & Tab 4.
  - Quản lý tích hợp GitHub, Pull Requests, bảng ma trận truy vết requirements.

---

## 3. Phần việc Người B: Dữ liệu và Công thức Điểm tương thích

### 3.1. Hệ thống 8 tiêu chí sinh hoạt và trọng số
Hệ thống chuẩn hóa 8 tiêu chí cốt lõi đại diện cho các xung đột KTX thường gặp:

| Tiêu chí | Trọng số gốc | Miền giá trị | Hàm đo độ tương đồng ($\text{sim} \in [0, 1]$) |
| :--- | :---: | :---: | :--- |
| **Giờ đi ngủ (`sleep`)** | 25% | $21.0 - 26.0$ | $\max(0, 1 - \|x.sleep - y.sleep\| / 5)$ |
| **Mức gọn gàng (`tidy`)** | 20% | $1 - 5$ | $1 - \|x.tidy - y.tidy\| / 4$ |
| **Mức chịu ồn (`noise`)** | 15% | $1 - 5$ | $1 - \|x.noise - y.noise\| / 4$ |
| **Giờ thức dậy (`wake`)** | 10% | $5.0 - 10.0$ | $\max(0, 1 - \|x.wake - y.wake\| / 5)$ |
| **Thói quen học (`study`)**| 10% | `phong`, `thuvien`, `it` | $1.0$ nếu trùng khớp, ngược lại $0.0$ |
| **Hút thuốc (`smoke`)** | 10% | $0$ (Không), $1$ (Có) | $1.0$ nếu cùng thói quen, ngược lại $0.0$ |
| **Khách về phòng (`guests`)**| 5% | $1 - 5$ | $1 - \|x.guests - y.guests\| / 4$ |
| **Sở thích (`hobbies`)** | 5% | Tập hợp danh mục | Chỉ số Jaccard: $\frac{\|x.hobbies \cap y.hobbies\|}{\|x.hobbies \cup y.hobbies\|}$ |

### 3.2. Công thức tính điểm tương thích bất đối xứng (`pair_score`)
Điểm số người $x$ đánh giá người $y$ được tính bằng:
$$\text{Score}(x, y) = 100 \times \frac{\sum_{k} w_k \cdot \text{sim}_k(x, y)}{\sum_k w_k}$$

**Nguyên lý bất đối xứng quan trọng:**
Nếu tiêu chí $k = x.top$ (tiêu chí cá nhân $x$ coi trọng nhất), trọng số của tiêu chí đó được nhân thêm hệ số **$1.5$**:
$$w_{x.top} = \text{WEIGHTS}[x.top] \times 1.5$$
Do $x.top$ có thể khác $y.top$, ta luôn có:
$$M[x][y] \neq M[y][x]$$
Điều này mô phỏng chính xác tâm lý con người trong thực tế: bạn có thể thấy một người rất hợp với mình, nhưng đối phương lại không thích bạn vì bạn không đáp ứng kỳ vọng hàng đầu của họ. Tính chất bất đối xứng này là điều kiện tiên quyết để việc xếp danh sách ưu tiên hai chiều của Gale-Shapley phát huy giá trị.

### 3.3. Thuật toán sinh dữ liệu giả lập 2 cụm (`generate_students`)
Để phản ánh đúng thực tế đời sống sinh viên, dữ liệu giả lập được sinh có cấu trúc phân cụm:
- **Cụm 1: "Cú đêm" (tỷ lệ 40%):** Giờ đi ngủ trung bình $25.0$ (1h sáng), tuân theo phân phối chuẩn $\mathcal{N}(25, 0.8^2)$.
- **Cụm 2: "Ngủ sớm" (tỷ lệ 60%):** Giờ đi ngủ trung bình $22.0$ (10h đêm), tuân theo phân phối chuẩn $\mathcal{N}(22, 0.8^2)$.
- **Giờ thức dậy tương quan sinh học:** $\text{wake} \approx \text{sleep} - 15 + \mathcal{N}(0, 0.7^2)$, phản ánh nhu cầu ngủ 7-8 tiếng mỗi ngày.

---

## 4. Phần việc Người A: Thuật toán Gale-Shapley và Phân tích

### 4.1. Cài đặt thuật toán Gale-Shapley tối ưu
- Cài đặt theo cơ chế **Người đề nghị hoãn chấp nhận (Deferred Acceptance)**.
- Xây dựng từ điển tra cứu thứ hạng nghịch đảo `rank_b[b][a]` tại bước khởi tạo giúp việc so sánh mức độ ưu tiên của sinh viên $b$ giữa ứng viên mới và đối tác hiện tại đạt độ phức tạp $\mathcal{O}(1)$.
- **Độ phức tạp tổng thể:** Thời gian $\mathcal{O}(N^2)$ và bộ nhớ $\mathcal{O}(N^2)$ với $N$ là số lượng sinh viên mỗi nhóm.

### 4.2. Định nghĩa Cặp chặn (*Blocking Pair*) và Kiểm chứng Ổn định (NFR-02)
Một cặp $(a, b)$ được gọi là một cặp chặn đối với phép ghép $M$ nếu:
1. $a$ và $b$ hiện không được ghép chung phòng với nhau: $M(a) \neq b$.
2. $a$ thích $b$ hơn người bạn cùng phòng hiện tại: $\text{rank}_a(b) < \text{rank}_a(M(a))$.
3. $b$ cũng thích $a$ hơn người bạn cùng phòng hiện tại: $\text{rank}_b(a) < \text{rank}_b(M(b))$.

Nếu tồn tại một cặp chặn, hai người này sẽ có động cơ "bỏ trốn" để ở cùng nhau, phá vỡ tính ổn định của ký túc xá.
* **Kết quả:** Hàm `count_blocking_pairs` được kiểm chứng tự động qua 50 seed ngẫu nhiên khác nhau, kết quả **số cặp chặn luôn bằng 0 tuyệt đối**.

### 4.3. Thuật toán gộp phòng 4 người (`merge_pairs_into_rooms`)
Để đáp ứng nhu cầu ký túc xá có phòng 4 giường, hệ thống áp dụng chiến lược gộp tham lam:
1. Mỗi cặp đôi 2 người $(p_1, p_2)$ được xem là một thực thể ghép.
2. Tính điểm tương thích trung bình giữa hai cặp $P$ và $Q$:
   $$\text{pair\_sim}(P, Q) = \frac{1}{4} \sum_{x \in P} \sum_{y \in Q} M[x][y]$$
3. Sắp xếp các liên kết cặp theo thứ tự giảm dần của độ tương hợp và gộp thành các phòng 4 người.

### 4.4. Đánh giá tính chất A-optimal và Hiệu năng NFR-01
- Thuật toán Gale-Shapley phiên bản nhóm A cầu hôn đem lại tính chất **A-optimal**: Nhóm A nhận được đối tác tốt nhất có thể trong tập hợp mọi phép ghép ổn định.
- Đo thời gian chạy thực nghiệm (`run_benchmark`):
  - Quy mô 100 sinh viên: $\approx 0.0006$ giây.
  - Quy mô 200 sinh viên: $\approx 0.0018$ giây.
  - Quy mô 400 sinh viên: $\approx 0.0072$ giây.
  - Quy mô 1000 sinh viên: $\approx 0.0450$ giây.  
  *(Vượt xa tiêu chuẩn NFR-01 yêu cầu xử lý dưới 5 giây).*

---

## 5. Phần việc Người C: Giải thích Cặp ghép và Thực nghiệm Đối chứng

### 5.1. Module giải thích minh bạch (`explain.py`)
Để giải tỏa sự tò mò và thắc mắc của sinh viên sau khi có danh sách phòng, module `explain.py` trích xuất:
- Các tiêu chí **Đồng thuận / Tương đồng cao** ($\text{sim}_k \ge 0.8$): Giúp hai bạn biết điểm mạnh chung để phát huy.
- Các tiêu chí **Cần lưu ý / Khác biệt** ($\text{sim}_k \le 0.4$): Giúp hai bạn biết trước sự khác nhau để chủ động thỏa thuận quy tắc sinh hoạt ngay từ đầu.
- Điểm đánh giá hai chiều $M[x][y]$ và $M[y][x]$.

### 5.2. Đánh giá độ thỏa mãn và Thực nghiệm so sánh (`evaluation.py`)
- **Chỉ số đo lường độ thỏa mãn trung bình:**
  $$\text{avg\_satisfaction}(match, M) = \frac{1}{2N} \sum_{(a, b) \in match} (M[a][b] + M[b][a])$$
- **Mô phỏng Monte-Carlo (`run_experiment`):**  
  Thực hiện so sánh giữa Gale-Shapley và Phép ghép ngẫu nhiên (chạy qua nhiều hạt giống ngẫu nhiên) ở các quy mô $N \in \{20, 50, 100, 200\}$:
  - Điểm thỏa mãn của Gale-Shapley luôn đạt **$\sim 72 - 76$ điểm**, cao hơn phương pháp ghép ngẫu nhiên (**$\sim 50 - 54$ điểm**) từ **25% đến 40%** (vượt xa chỉ tiêu BR-01 yêu cầu tăng $\ge 20\%$).
  - Số cặp chặn của ghép ngẫu nhiên luôn ở mức cao (thường từ 30% đến 60% quy mô ghép), trong khi Gale-Shapley luôn giữ mức 0.

---

## 6. Phân tích Hạn chế Mô hình Hai phía và So sánh Thuật toán Stable Roommates

### 6.1. Hạn chế cốt lõi của giả định Bipartite (Hai phía)
Mô hình Gale-Shapley áp dụng cho bài toán này giả định sinh viên được chia thành hai tập hợp rời rạc: Nhóm A (chủ động đề nghị) và Nhóm B (xét duyệt đề nghị).
- **Ý nghĩa thực tế:** Có thể phân chia theo: Khóa cũ ghép với Khóa mới (để khóa cũ hướng dẫn khóa mới), hoặc Sinh viên hướng nội ghép với Sinh viên hướng ngoại, hoặc phân theo khối ngành.
- **Hạn chế:** Trong thực tế ký túc xá tổng quát, sinh viên là một tập hợp thuần nhất (Unipartite). Bất kỳ ai cũng có thể ở chung phòng với bất kỳ ai khác mà không bị bó hẹp trong việc phải ghép với người thuộc nhóm đối diện.

### 6.2. Đối chiếu với Bài toán Stable Roommates và Thuật toán Irving (1985)
Khi bài toán không phân chia thành hai nhóm A và B, bài toán trở thành **Bài toán Bạn cùng phòng Ổn định (*Stable Roommates Problem*)**:
1. **Thuật toán Irving (1985):** Là giải thuật giải bài toán Stable Roommates gồm 2 giai đoạn:
   - *Giai đoạn 1:* Tương tự Gale-Shapley, các cá nhân đề nghị lẫn nhau để rút gọn danh sách ưu tiên.
   - *Giai đoạn 2:* Tìm và loại trừ các chu trình xoay vòng (all-or-nothing cycles).
2. **Khác biệt cốt lõi về sự tồn tại của nghiệm:**
   - Trong Gale-Shapley (Hai phía): **Luôn luôn tồn tại ít nhất một phép ghép ổn định** đối với mọi danh sách ưu tiên.
   - Trong Irving (Một phía): **Không đảm bảo luôn có nghiệm**. Tồn tại những cấu hình danh sách ưu tiên có chu trình lẻ (odd cycles) khiến không có bất kỳ phép ghép nào đạt trạng thái ổn định (thuật toán Irving sẽ trả về vô nghiệm).
3. **Đánh giá quyết định thiết kế:**
   Việc chọn mô hình Gale-Shapley chia 2 nhóm cho đồ án này là một quyết định kỹ thuật hợp lý: Đảm bảo hệ thống **luôn luôn tìm ra giải pháp phân phòng ổn định tuyệt đối**, thời gian thực thi nhanh $\mathcal{O}(N^2)$, dễ dàng triển khai thực tế và kiểm chứng tính đúng đắn toán học một cách chặt chẽ.

---

## 7. Ma trận Truy vết và Kết quả Kiểm thử Toàn diện

### 7.1. Bảng ma trận truy vết (Requirements Traceability Matrix)

| Mã BR | Yêu cầu Nghiệp vụ (BR) | Mã SR | Yêu cầu Bên liên quan (SR) | Mã FR | Chức năng (FR) | Kiểm chứng qua Test |
| :---: | :--- | :---: | :--- | :---: | :--- | :--- |
| **BR-01** | Giảm xung đột, điểm hài lòng tăng $\ge 20\%$ so với ngẫu nhiên | **SR-01** | Khảo sát 8 tiêu chí và tiêu chí `top` | **FR-01**<br>**FR-04** | Nhập form; Tính `pair_score` bất đối xứng | `tests/test_scoring.py`<br>`tests/test_perf_scoring.py` |
| **BR-01** | Minh bạch hóa lý do ghép phòng cho sinh viên | **SR-02**<br>**SR-03** | Xem bạn ghép, điểm 2 chiều và tiêu chí trùng/lưu ý | **FR-09** | Giải thích cặp ghép `explain_pair` | `tests/test_explain.py`<br>Giao diện Tab 3 |
| **BR-02** | Xếp phòng ổn định tuyệt đối (0 cặp chặn) | **SR-05** | Chạy thuật toán ghép hai phía ổn định | **FR-06**<br>**FR-08** | Gale-Shapley; `count_blocking_pairs` | `tests/test_matching.py` (50 seed xanh 100%) |
| **BR-03** | Tối ưu hóa quy trình phân phòng cho BQL KTX | **SR-04** | Nạp CSV hoặc sinh giả lập có `seed` | **FR-02**<br>**FR-03** | `load_students_csv`; `generate_students` | `tests/test_data_io.py`<br>`tests/test_error_handling.py` |
| **BR-03** | Đánh giá trực quan và xuất file | **SR-06**<br>**SR-08** | Biểu đồ đối chứng và tải kết quả CSV | **FR-10**<br>**FR-11** | `run_experiment`; Tải CSV Tab 2 & 3 | `tests/test_evaluation.py`<br>`tests/test_benchmark.py` |
| **BR-04** | Kiểm thử tự động và minh bạch hệ thống | **SR-07** | CI/CD và văn hóa cộng tác mã nguồn | - | Bộ unit test toàn diện; Lịch sử Git PR | Toàn bộ thư mục `tests/` |

### 7.2. Kết quả kiểm thử tự động (`pytest -v`)
Hệ thống tích hợp 31 unit test bao phủ toàn bộ các module và ngoại lệ:

```text
tests/test_benchmark.py::test_run_benchmark_keys_and_values PASSED          [  3%]
tests/test_benchmark.py::test_benchmark_under_one_second_for_small_n PASSED [  6%]
tests/test_benchmark.py::test_stress_1000_students_under_5_seconds PASSED  [  9%]
tests/test_data_io.py::test_load_students_csv_valid PASSED                 [ 12%]
tests/test_data_io.py::test_load_students_csv_missing_columns PASSED        [ 16%]
tests/test_data_io.py::test_load_students_csv_invalid_types PASSED          [ 19%]
tests/test_data_io.py::test_load_students_csv_rejects_empty_file PASSED     [ 22%]
tests/test_data_io.py::test_generate_students_count_and_groups PASSED      [ 25%]
tests/test_data_io.py::test_generate_students_reproducibility PASSED        [ 29%]
tests/test_data_io.py::test_generate_students_valid_ranges PASSED           [ 32%]
tests/test_error_handling.py::test_error_missing_cols_csv PASSED            [ 35%]
tests/test_error_handling.py::test_error_invalid_types_csv PASSED          [ 38%]
tests/test_error_handling.py::test_error_empty_csv PASSED                  [ 41%]
tests/test_error_handling.py::test_unbalanced_groups_handling PASSED        [ 45%]
tests/test_evaluation.py::test_avg_satisfaction_range PASSED               [ 48%]
tests/test_evaluation.py::test_avg_satisfaction_empty PASSED               [ 51%]
tests/test_evaluation.py::test_run_experiment_structure PASSED             [ 54%]
tests/test_evaluation.py::test_gale_shapley_beats_random PASSED            [ 58%]
tests/test_explain.py::test_explain_pair_identical PASSED                   [ 61%]
tests/test_explain.py::test_explain_pair_conflicting PASSED                 [ 64%]
tests/test_explain.py::test_explain_pair_returns_both_scores PASSED        [ 67%]
tests/test_matching.py::test_gale_shapley_is_stable PASSED                 [ 70%]
tests/test_matching.py::test_random_usually_unstable PASSED                [ 74%]
tests/test_matching.py::test_analyze_matching_quality_perfect PASSED       [ 77%]
tests/test_matching.py::test_merge_pairs_into_rooms_4 PASSED               [ 80%]
tests/test_perf_scoring.py::test_scoring_perf_200_students PASSED           [ 83%]
tests/test_scoring.py::test_identical_students_score_100 PASSED            [ 87%]
tests/test_scoring.py::test_pair_score_range PASSED                         [ 90%]
tests/test_scoring.py::test_top_criterion_boost PASSED                      [ 93%]
tests/test_scoring.py::test_asymmetry_between_students PASSED               [ 96%]
tests/test_scoring.py::test_build_pref_lists_valid PASSED                   [100%]

============================= 31 passed in 1.25s ==============================
```

---

## 8. Kết luận và Hướng phát triển

### 8.1. Đóng góp của Đồ án
1. **Cơ sở khoa học vững chắc:** Ứng dụng thành công lý thuyết trò chơi và kinh tế học ghép cặp (giải Nobel Kinh tế 2012 của Alvin Roth & Lloyd Shapley) vào giải quyết bài toán thực tế trong quản lý sinh viên.
2. **Kỹ thuật phần mềm chuẩn mực:** Thực hiện trọn vẹn quy trình công nghệ phần mềm: từ yêu cầu (BR, FR, SR, IR), mô hình hóa toán học, mã nguồn kiểm thử tự động đến giao diện người dùng và ma trận truy vết.
3. **Hiệu năng xuất sắc:** Tốc độ xử lý tính bằng mili-giây, giao diện web Streamlit trực quan, minh bạch lý do ghép phòng.

### 8.2. Hướng phát triển tương lai
- Nghiên cứu cài đặt giải thuật **Irving (1985)** có cơ chế xử lý chu trình lẻ để hỗ trợ mô hình bạn cùng phòng không phân nhóm.
- Mở rộng hỗ trợ ràng buộc cứng đặc biệt (ví dụ: yêu cầu sinh viên phải ở cùng tòa nhà, cùng tầng, hoặc theo nguyện vọng trường học cụ thể).
- Phát triển API RESTful bằng FastAPI để tích hợp trực tiếp vào Cổng thông tin đào tạo của Nhà trường.
