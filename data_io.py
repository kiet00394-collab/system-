import random
from typing import List, Union, TextIO
import pandas as pd
from models import Student

HOBBIES = ["game", "nhac", "the thao", "phim", "doc sach", "nau an"]
REQUIRED = ["id", "name", "group", "sleep", "wake", "tidy", "study", "noise", "smoke", "guests", "hobbies", "top"]
VALID_STUDY = {"phong", "thuvien", "it"}

def load_students_csv(path_or_file: Union[str, TextIO]) -> List[Student]:
    """
    Đọc dữ liệu sinh viên từ file CSV hoặc upload buffer.
    Kiểm tra đầy đủ các ràng buộc dữ liệu (NFR-04):
    - Đủ các cột bắt buộc
    - File không rỗng
    - Đúng định dạng kiểu dữ liệu từng trường
    - Thuộc miền giá trị hợp lệ
    """
    try:
        df = pd.read_csv(path_or_file)
    except Exception as e:
        raise ValueError(f"Không thể đọc file CSV: {e}")

    if df.empty or len(df) == 0:
        raise ValueError("File CSV rỗng, không chứa dữ liệu sinh viên.")

    missing = [c for c in REQUIRED if c not in df.columns]
    if missing:
        raise ValueError(f"Thiếu các cột bắt buộc: {', '.join(missing)}")

    students = []
    for idx, r in enumerate(df.itertuples(index=False)):
        row_num = idx + 2  # Dòng thực tế trong file Excel/CSV (tính cả header)
        
        # Kiểm tra nhóm
        group_val = str(r.group).strip().upper()
        if group_val not in ("A", "B"):
            raise ValueError(f"Dòng {row_num}: Cột 'group' phải là 'A' hoặc 'B' (nhận được '{r.group}')")

        # Kiểm tra kiểu số và miền giá trị
        try:
            sleep_val = float(r.sleep)
            wake_val = float(r.wake)
        except (ValueError, TypeError):
            raise ValueError(f"Dòng {row_num}: 'sleep' và 'wake' phải là số thực hợp lệ.")

        try:
            tidy_val = int(r.tidy)
            noise_val = int(r.noise)
            smoke_val = int(r.smoke)
            guests_val = int(r.guests)
        except (ValueError, TypeError):
            raise ValueError(f"Dòng {row_num}: 'tidy', 'noise', 'smoke', 'guests' phải là số nguyên.")

        hobbies_set = set()
        if pd.notna(r.hobbies) and str(r.hobbies).strip():
            hobbies_set = {h.strip() for h in str(r.hobbies).split(";") if h.strip()}

        students.append(Student(
            id=idx,
            name=str(r.name),
            group=group_val,
            sleep=sleep_val,
            wake=wake_val,
            tidy=tidy_val,
            study=str(r.study).strip(),
            noise=noise_val,
            smoke=smoke_val,
            guests=guests_val,
            hobbies=hobbies_set,
            top=str(r.top).strip()
        ))

    return students

def generate_students(n: int, seed: int = 42) -> List[Student]:
    """
    Sinh danh sách N sinh viên giả lập, chia đều nhóm A và B.
    Mô phỏng 2 cụm 'cú đêm' (40%) và 'ngủ sớm' (60%) theo phân phối Gauss.
    """
    rng = random.Random(seed)
    students = []
    for i in range(n):
        night_owl = rng.random() < 0.4
        sleep = rng.gauss(25 if night_owl else 22, 0.8)
        sleep_val = min(26.0, max(21.0, round(sleep, 1)))
        wake_val = min(10.0, max(5.0, round(sleep_val - 15 + rng.gauss(0, 0.7), 1)))

        students.append(Student(
            id=i,
            name=f"SV{i:03d}",
            group="A" if i % 2 == 0 else "B",
            sleep=sleep_val,
            wake=wake_val,
            tidy=rng.randint(1, 5),
            study=rng.choice(["phong", "thuvien", "it"]),
            noise=rng.randint(1, 5),
            smoke=int(rng.random() < 0.1),
            guests=rng.randint(1, 5),
            hobbies=set(rng.sample(HOBBIES, rng.randint(1, 3))),
            top=rng.choice(["sleep", "tidy", "noise", "study", "smoke"])
        ))
    return students

def students_to_dataframe(students: List[Student]) -> pd.DataFrame:
    """Chuyển danh sách Student thành DataFrame hiển thị trên Streamlit."""
    return pd.DataFrame([
        {
            **s.__dict__,
            "hobbies": ";".join(sorted(s.hobbies))
        } for s in students
    ])
