# Hệ thống Ghép phòng Ký túc xá Tự động (Gale-Shapley Dorm Matching)

> **Môn học:** System Engineering  
> **Đề tài:** Xây dựng hệ thống ghép phòng ký túc xá tự động dựa trên thuật toán Gale-Shapley  
> **Ngôn ngữ & Công nghệ:** Python 3.11+, Streamlit, Pandas, NumPy, Matplotlib, Pytest  

---

## 1. Giới thiệu Đề tài

Trong các ký túc xá đại học, việc phân bổ phòng thủ công hoặc ngẫu nhiên thường dẫn tới xung đột thói quen sinh hoạt (giờ giấc ngủ, độ ngăn nắp, tiếng ồn, thói quen học tập, hút thuốc...). Dự án xây dựng một giải pháp phần mềm tự động hóa quá trình ghép phòng hai phía (Two-sided Matching) dựa trên:
1. Thu thập dữ liệu khảo sát sinh hoạt gồm **8 tiêu chí cốt lõi**.
2. Tính toán ma trận độ tương thích hai chiều \(M[i][j]\) có xét đến tiêu chí ưu tiên cá nhân (`top`).
3. Ứng dụng thuật toán ghép cặp ổn định **Gale-Shapley** nhằm triệt tiêu hoàn toàn các cặp chặn (Blocking Pairs = 0).
4. Minh bạch hóa lý do ghép phòng và trực quan hóa thực nghiệm so sánh với phương pháp ghép ngẫu nhiên.

---

## 2. Phân công Thành viên

| Thành viên | Vai trò | Phụ trách Module | Giao diện | Tài liệu & Báo cáo |
| :--- | :---: | :--- | :--- | :--- |
| **Bùi Đình Hiếu** | **Người A** | `matching.py`, `tests/test_matching.py` | Tab 2: "Ghép phòng" | NFR, Lý thuyết & Thuật toán |
| **Châu Tuấn Kiệt** | **Người B** | `models.py`, `data_io.py`, `scoring.py`, `tests/test_scoring.py` | Tab 1: "Dữ liệu" | BR, FR, Dữ liệu & Công thức điểm |
| **Hoàng Triều** | **Người C** | `explain.py`, `evaluation.py`, Quản lý Repo | Tab 3: "Giải thích", Tab 4: "So sánh" | SR, IR, Ma trận truy vết, Video & Báo cáo tổng hợp |

---

## 3. Cấu trúc Thư mục Dự án

```text
system-/
├── app.py                     # Entry point chính chạy ứng dụng Streamlit (C)
├── models.py                  # Định nghĩa dataclass Student (B)
├── data_io.py                 # Đọc CSV, sinh dữ liệu giả lập (B)
├── scoring.py                 # Tính toán similarity và ma trận điểm M (B)
├── matching.py                # Thuật toán Gale-Shapley & đếm cặp chặn (A)
├── explain.py                 # Diễn giải tiêu chí trùng khớp và cần lưu ý (C)
├── evaluation.py              # Đánh giá độ hài lòng & thực nghiệm so sánh (C)
├── ui/                        # Các module giao diện Streamlit
│   ├── __init__.py
│   ├── tab_data.py            # Giao diện Tab 1: Nạp & sinh dữ liệu (B)
│   ├── tab_match.py           # Giao diện Tab 2: Ghép phòng Gale-Shapley (A)
│   ├── tab_explain.py         # Giao diện Tab 3: Giải thích cặp ghép (C)
│   └── tab_compare.py         # Giao diện Tab 4: Biểu đồ so sánh thực nghiệm (C)
├── tests/                     # Bộ kiểm thử tự động (Pytest)
│   ├── test_data_io.py
│   ├── test_scoring.py
│   ├── test_matching.py
│   └── test_error_handling.py
├── data/                      # Dữ liệu mẫu và dữ liệu kiểm thử
│   ├── sample_students.csv
│   └── error_*.csv
├── docs/                      # Tài liệu phân tích và kỹ thuật (SRS, BR, FR, SR, IR, NFR)
│   ├── BR_FR.md
│   ├── SR_IR.md
│   ├── NFR.md
│   ├── ly_thuyet.md
│   └── truy_vet.md
├── requirements.txt           # Danh mục thư viện phụ thuộc
└── README.md                  # Hướng dẫn dự án
```

---

## 4. Hướng dẫn Cài đặt & Khởi chạy

### Bước 1: Chuẩn bị môi trường
Yêu cầu máy tính đã cài đặt **Python 3.10** hoặc **3.11** và **Git**.

### Bước 2: Clone repository & Tạo môi trường ảo
```bash
# Clone repository về máy
git clone https://github.com/kiet00394-collab/system-.git
cd system-

# Khởi tạo môi trường ảo Python
python -m venv .venv

# Kích hoạt môi trường ảo
# Trên Windows (PowerShell):
.venv\Scripts\Activate.ps1
# Trên Windows (CMD):
.venv\Scripts\activate.bat
# Trên macOS / Linux:
source .venv/bin/activate
```

### Bước 3: Cài đặt các thư viện phụ thuộc
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Bước 4: Chạy kiểm thử tự động (Unit Test)
```bash
pytest -v
```

### Bước 5: Khởi chạy ứng dụng Streamlit
```bash
streamlit run app.py
```
Ứng dụng sẽ tự động mở trên trình duyệt tại địa chỉ: `http://localhost:8501`.

---

## 5. Định dạng Dữ liệu Khảo sát Đầu vào (`.csv`)

Mỗi dòng đại diện cho một sinh viên với 12 thuộc tính:

| Cột | Ý nghĩa | Miền giá trị |
| :--- | :--- | :--- |
| `id` | Mã định danh sinh viên | Số nguyên duy nhất: `0, 1, 2, ...` |
| `name` | Tên sinh viên | Chuỗi ký tự (ví dụ: `Nguyen Van An`) |
| `group` | Phân nhóm ghép hai phía | `"A"` (sinh viên cũ) hoặc `"B"` (sinh viên mới) |
| `sleep` | Giờ đi ngủ | Số thực từ `21.0` đến `26.0` (`26.0` = 2h sáng) |
| `wake` | Giờ thức dậy | Số thực từ `5.0` đến `10.0` |
| `tidy` | Mức độ gọn gàng ngăn nắp | Thang điểm `1` (bừa bộn) đến `5` (rất sạch sẽ) |
| `study` | Địa điểm/Thói quen học tập | `"phong"`, `"thuvien"`, hoặc `"it"` |
| `noise` | Mức độ chịu ồn | Thang điểm `1` (cần yên tĩnh) đến `5` (thoải mái ồn) |
| `smoke` | Tình trạng hút thuốc | `0` (không hút thuốc), `1` (có hút thuốc) |
| `guests` | Tần suất dắt bạn về phòng | Thang điểm `1` (hiếm khi) đến `5` (thường xuyên) |
| `hobbies` | Sở thích cá nhân | Tách bằng dấu chấm phẩy `;` (ví dụ: `game;nhac;the thao`) |
| `top` | Tiêu chí quan trọng nhất | Một trong 8 tiêu chí: `sleep`, `wake`, `tidy`, `study`, `noise`, `smoke`, `guests`, `hobbies` |

---

## 6. Quy trình Làm việc với Git

* **Nguyên tắc vàng:** Không ai commit trực tiếp vào nhánh `main`. Toàn bộ tính năng đi qua **Pull Request (PR)**.
* **Định danh nhánh:** `feature/<ten-nguoi-phu-trach>-<ten-tinh-nang>` (Ví dụ: `feature/c-explain-evaluation`).
* **Quy trình chuẩn:**
  1. `git checkout main && git pull origin main`
  2. `git checkout -b feature/<ten-tinh-nang>`
  3. Viết code, chạy test `pytest -v` đảm bảo xanh.
  4. `git commit -m "feat/fix/docs: mô tả rõ ràng"`
  5. `git push -u origin feature/<ten-tinh-nang>`
  6. Mở Pull Request trên GitHub, gắn reviewer xoay vòng (A review B, B review C, C review A).
