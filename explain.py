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
    Sinh chuỗi giải thích lý do ghép cặp chi tiết giữa hai sinh viên x và y.
    - Tiêu chí trùng khớp nổi bật: similarity >= 0.8
    - Tiêu chí khác biệt cần lưu ý: similarity <= 0.4
    - Phân tích mức độ đáp ứng tiêu chí ưu tiên nhất (top) của từng bạn.
    """
    sims = criterion_sims(x, y)
    good = [LABELS[k] for k, v in sims.items() if v >= 0.8]
    bad = [LABELS[k] for k, v in sims.items() if v <= 0.4]

    text = f"Trùng khớp: {', '.join(good) if good else 'không có tiêu chí nổi bật'}."
    if bad:
        text += f" Cần lưu ý: {', '.join(bad)}."

    # Phân tích mức độ đáp ứng tiêu chí ưu tiên cá nhân (top)
    top_x_lbl = LABELS.get(x.top, x.top)
    top_y_lbl = LABELS.get(y.top, y.top)
    sim_top_x = sims.get(x.top, 0.0) * 100
    sim_top_y = sims.get(y.top, 0.0) * 100

    pref_details = (
        f" Tiêu chí ưu tiên: {x.name} quan tâm nhất '{top_x_lbl}' (đáp ứng {sim_top_x:.0f}%); "
        f"{y.name} quan tâm nhất '{top_y_lbl}' (đáp ứng {sim_top_y:.0f}%)."
    )
    text += pref_details
    return text
