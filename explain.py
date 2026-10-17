from typing import Dict
from models import Student
from scoring import criterion_sims

LABELS: Dict[str, str] = {
    "sleep": "giờ đi ngủ",
    "wake": "giờ thức dậy",
    "tidy": "mức gọn gàng",
    "study": "thói quen học",
    "noise": "mức ồn",
    "smoke": "hút thuốc",
    "guests": "mức hay có khách",
    "hobbies": "sở thích"
}

def explain_pair(x: Student, y: Student) -> str:
    """
    Sinh chuỗi giải thích lý do ghép cặp giữa hai sinh viên x và y.
    - Tiêu chí trùng khớp nổi bật: similarity >= 0.8
    - Tiêu chí khác biệt cần lưu ý: similarity <= 0.4
    """
    sims = criterion_sims(x, y)
    good = [LABELS[k] for k, v in sims.items() if v >= 0.8]
    bad = [LABELS[k] for k, v in sims.items() if v <= 0.4]

    text = f"Trùng khớp: {', '.join(good) if good else 'không có tiêu chí nổi bật'}."
    if bad:
        text += f" Cần lưu ý: {', '.join(bad)}."
    return text
