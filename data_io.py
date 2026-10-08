import random
import pandas as pd
from models import Student

HOBBIES = ["game", "nhac", "the thao", "phim", "doc sach", "nau an"]
REQUIRED = ["id", "name", "group", "sleep", "wake", "tidy", "study", "noise", "smoke", "guests", "hobbies", "top"]

def load_students_csv(path_or_file) -> list[Student]:
    df = pd.read_csv(path_or_file)
    missing = [c for c in REQUIRED if c not in df.columns]
    if missing:
        raise ValueError(f"Thiếu các cột bắt buộc: {missing}")

    students = []
    for i, r in enumerate(df.itertuples(index=False)):
        hobbies_set = set()
        if pd.notna(r.hobbies) and str(r.hobbies).strip():
            hobbies_set = set(str(r.hobbies).split(";"))

        students.append(Student(
            id=i,
            name=str(r.name),
            group=str(r.group).strip().upper(),
            sleep=float(r.sleep),
            wake=float(r.wake),
            tidy=int(r.tidy),
            study=str(r.study),
            noise=int(r.noise),
            smoke=int(r.smoke),
            guests=int(r.guests),
            hobbies=hobbies_set,
            top=str(r.top)
        ))
    return students

def generate_students(n: int, seed: int = 42) -> list[Student]:
    rng = random.Random(seed)
    students = []
    for i in range(n):
        night_owl = rng.random() < 0.4           # tạo 2 cụm "cú đêm" và "ngủ sớm"
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

def students_to_dataframe(students: list[Student]) -> pd.DataFrame:
    return pd.DataFrame([
        {
            **s.__dict__,
            "hobbies": ";".join(sorted(s.hobbies))
        } for s in students
    ])
