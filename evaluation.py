from typing import Dict, Any, Tuple
import numpy as np
from data_io import generate_students
from scoring import compute_score_matrix, build_pref_lists
from matching import gale_shapley, random_matching, count_blocking_pairs

def avg_satisfaction(match: Dict[int, int], M: np.ndarray) -> float:
    """
    Tính điểm hài lòng trung bình của các sinh viên được ghép chung phòng.
    Là trung bình cộng điểm số đánh giá hai chiều: M[a][b] và M[b][a].
    """
    if not match:
        return 0.0
    scores = [M[a][b] for a, b in match.items()] + [M[b][a] for a, b in match.items()]
    return float(np.mean(scores))

def group_satisfaction(match: Dict[int, int], M: np.ndarray) -> Tuple[float, float]:
    """
    Tính điểm hài lòng trung bình riêng rẽ của từng nhóm:
    - sat_a: Điểm nhóm A (bên chủ động đề nghị) đánh giá bạn cùng phòng nhóm B.
    - sat_b: Điểm nhóm B (bên bị động chấp thuận) đánh giá bạn cùng phòng nhóm A.
    Giúp đo lường tính chất A-optimal vs B-pessimal của thuật toán Gale-Shapley.
    """
    if not match:
        return 0.0, 0.0
    sat_a = float(np.mean([M[a][b] for a, b in match.items()]))
    sat_b = float(np.mean([M[b][a] for a, b in match.items()]))
    return sat_a, sat_b

def run_experiment(n: int, seed: int = 0, n_random: int = 100) -> Dict[str, Any]:
    """
    Chạy thử nghiệm so sánh giữa thuật toán Gale-Shapley và phương pháp ghép ngẫu nhiên.
    - n: Số lượng sinh viên (chia đều cho 2 nhóm A và B).
    - seed: Seed sinh dữ liệu giả lập.
    - n_random: Số lần lặp ghép ngẫu nhiên để lấy điểm trung bình đối chứng.
    """
    students = generate_students(n, seed)
    M = compute_score_matrix(students)
    pa, pb = build_pref_lists(M, students)

    # Chạy thuật toán Gale-Shapley
    gs_match = gale_shapley(pa, pb)
    gs_satisfaction = avg_satisfaction(gs_match, M)
    gs_sat_a, gs_sat_b = group_satisfaction(gs_match, M)
    blocking_count = count_blocking_pairs(gs_match, pa, pb)

    # Chạy ghép ngẫu nhiên n_random lần để lấy trung bình
    rand_scores = [
        avg_satisfaction(random_matching(pa, pb, seed=s), M)
        for s in range(n_random)
    ]
    random_satisfaction = float(np.mean(rand_scores))

    return {
        "n": n,
        "gs": round(gs_satisfaction, 2),
        "gs_a": round(gs_sat_a, 2),
        "gs_b": round(gs_sat_b, 2),
        "a_bias": round(gs_sat_a - gs_sat_b, 2),
        "random": round(random_satisfaction, 2),
        "blocking_pairs": blocking_count,
    }
