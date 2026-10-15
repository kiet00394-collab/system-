from typing import List, Dict, Tuple
import numpy as np
from models import Student

# Trọng số mặc định của 8 tiêu chí sinh hoạt
WEIGHTS = {
    "sleep": 0.25,    # Giờ đi ngủ (25%) - tiêu chí quan trọng hàng đầu
    "wake": 0.10,     # Giờ thức dậy (10%)
    "tidy": 0.20,     # Mức độ gọn gàng (20%) - nguyên nhân xung đột thường gặp
    "study": 0.10,    # Thói quen học tập (10%)
    "noise": 0.15,    # Khả năng chịu ồn (15%)
    "smoke": 0.10,    # Hút thuốc (10%) - ảnh hưởng sức khỏe & mùi phòng
    "guests": 0.05,   # Tần suất dắt bạn về phòng (5%)
    "hobbies": 0.05   # Sở thích chung (5%) - tạo gắn kết xã hội
}

def criterion_sims(x: Student, y: Student) -> Dict[str, float]:
    """
    Tính độ tương đồng (similarity) giữa hai sinh viên x và y trên từng tiêu chí.
    Giá trị trả về nằm trong đoạn [0.0, 1.0], với 1.0 là hoàn toàn trùng khớp.
    """
    clip = lambda v: max(0.0, min(1.0, float(v)))
    union = x.hobbies | y.hobbies

    return {
        "sleep": clip(1.0 - abs(x.sleep - y.sleep) / 5.0),
        "wake": clip(1.0 - abs(x.wake - y.wake) / 5.0),
        "tidy": clip(1.0 - abs(x.tidy - y.tidy) / 4.0),
        "study": 1.0 if x.study == y.study else 0.0,
        "noise": clip(1.0 - abs(x.noise - y.noise) / 4.0),
        "smoke": 1.0 if x.smoke == y.smoke else 0.0,
        "guests": clip(1.0 - abs(x.guests - y.guests) / 4.0),
        "hobbies": float(len(x.hobbies & y.hobbies) / len(union)) if union else 0.0,
    }

def pair_score(x: Student, y: Student, weights: Dict[str, float] = WEIGHTS) -> float:
    """
    Tính điểm số mà sinh viên x đánh giá mức độ phù hợp của bạn cùng phòng y.
    Thang điểm [0.0, 100.0].
    
    Đặc điểm cốt lõi: Tiêu chí cá nhân quan trọng nhất (x.top) được nhân hệ số 1.5.
    Điều này tạo nên tính chất bất đối xứng: M[x][y] không nhất thiết bằng M[y][x],
    phản ánh góc nhìn và kỳ vọng riêng của từng người.
    """
    w = dict(weights)
    if x.top in w:
        w[x.top] *= 1.5

    total_weight = sum(w.values())
    sims = criterion_sims(x, y)
    score = 100.0 * sum(w[k] * sims[k] for k in w) / total_weight
    return round(score, 2)

def compute_score_matrix(students: List[Student], weights: Dict[str, float] = WEIGHTS) -> np.ndarray:
    """
    Tính toán ma trận tương thích toàn thể M kích thước N x N.
    Trong đó:
    - M[i][j]: Điểm sinh viên i đánh giá sinh viên j.
    - M[i][i] = 0.0 (không tự đánh giá bản thân).
    """
    n = len(students)
    M = np.zeros((n, n), dtype=float)
    for i in range(n):
        for j in range(n):
            if i != j:
                M[i][j] = pair_score(students[i], students[j], weights)
    return M

def build_pref_lists(
    M: np.ndarray, 
    students: List[Student]
) -> Tuple[Dict[int, List[int]], Dict[int, List[int]]]:
    """
    Xây dựng danh sách ưu tiên hai phía cho thuật toán Gale-Shapley:
    - pref_a: Dict[id_A -> list ID các bạn nhóm B, sắp xếp theo điểm M[a][b] giảm dần].
    - pref_b: Dict[id_B -> list ID các bạn nhóm A, sắp xếp theo điểm M[b][a] giảm dần].
    """
    ids_a = [s.id for s in students if s.group == "A"]
    ids_b = [s.id for s in students if s.group == "B"]

    pref_a = {a: sorted(ids_b, key=lambda b: -M[a][b]) for a in ids_a}
    pref_b = {b: sorted(ids_a, key=lambda a: -M[b][a]) for b in ids_b}

    return pref_a, pref_b

def analyze_score_asymmetry(M: np.ndarray, students: List[Student]) -> Dict[str, float]:
    """
    Phân tích tỷ lệ bất đối xứng điểm số trong ma trận M để chứng minh tính hai phía của bài toán.
    """
    n = len(students)
    diffs = []
    asymmetric_count = 0
    total_pairs = 0

    for i in range(n):
        for j in range(i + 1, n):
            diff = abs(M[i][j] - M[j][i])
            diffs.append(diff)
            if diff > 0.01:
                asymmetric_count += 1
            total_pairs += 1

    return {
        "total_pairs": total_pairs,
        "asymmetric_pairs": asymmetric_count,
        "asymmetry_ratio": round(asymmetric_count / total_pairs, 4) if total_pairs else 0.0,
        "mean_diff": round(float(np.mean(diffs)), 2) if diffs else 0.0,
        "max_diff": round(float(np.max(diffs)), 2) if diffs else 0.0
    }
