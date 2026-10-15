import numpy as np
from models import Student
from data_io import generate_students
from scoring import (
    criterion_sims, 
    pair_score, 
    compute_score_matrix, 
    build_pref_lists, 
    analyze_score_asymmetry
)

def test_identical_students_score_100():
    """Hai sinh viên có toàn bộ 8 tiêu chí giống hệt nhau phải đạt điểm 100."""
    s1 = Student(0, "An", "A", 22.0, 7.0, 4, "phong", 2, 0, 1, {"game", "nhac"}, "sleep")
    s2 = Student(1, "Bình", "B", 22.0, 7.0, 4, "phong", 2, 0, 1, {"game", "nhac"}, "sleep")

    score = pair_score(s1, s2)
    assert score == 100.0, f"Expected 100.0, got {score}"

def test_opposite_students_score_near_zero():
    """Hai sinh viên có các tiêu chí đối lập tối đa phải có điểm tương thích bằng hoặc xấp xỉ 0."""
    s1 = Student(0, "A", "A", 21.0, 5.0, 1, "phong", 1, 0, 1, {"game"}, "sleep")
    s2 = Student(1, "B", "B", 26.0, 10.0, 5, "thuvien", 5, 1, 5, {"the thao"}, "smoke")
    
    score = pair_score(s1, s2)
    assert 0.0 <= score <= 5.0, f"Expected near 0, got {score}"

def test_different_students_score_asymmetry():
    """Kiểm tra tính bất đối xứng: Hai sinh viên có tiêu chí top khác nhau sẽ có điểm chéo khác nhau."""
    s1 = Student(0, "An", "A", 22.0, 7.0, 5, "phong", 1, 0, 1, {"game"}, "tidy")
    s2 = Student(1, "Bình", "B", 22.0, 7.0, 4, "phong", 1, 0, 1, {"game"}, "smoke")

    score_12 = pair_score(s1, s2)
    score_21 = pair_score(s2, s1)

    assert 0.0 <= score_12 <= 100.0
    assert 0.0 <= score_21 <= 100.0
    assert score_12 != score_21

def test_compute_score_matrix_and_pref_lists():
    """Kiểm tra ma trận điểm NxN và danh sách ưu tiên xếp đúng thứ tự giảm dần."""
    students = generate_students(10, seed=42)
    M = compute_score_matrix(students)

    assert M.shape == (10, 10)
    for i in range(10):
        assert M[i][i] == 0.0  # Self-score should be 0

    pref_a, pref_b = build_pref_lists(M, students)

    # Check group A preferences
    ids_b = [s.id for s in students if s.group == "B"]
    ids_a = [s.id for s in students if s.group == "A"]

    assert len(pref_a) == len(ids_a)
    assert len(pref_b) == len(ids_b)

    for a, lst in pref_a.items():
        assert set(lst) == set(ids_b)
        scores = [M[a][b] for b in lst]
        assert scores == sorted(scores, reverse=True)

    for b, lst in pref_b.items():
        assert set(lst) == set(ids_a)
        scores = [M[b][a] for a in lst]
        assert scores == sorted(scores, reverse=True)

def test_analyze_score_asymmetry():
    """Kiểm tra hàm phân tích tính bất đối xứng trên tập mẫu 20 sinh viên."""
    students = generate_students(20, seed=42)
    M = compute_score_matrix(students)
    metrics = analyze_score_asymmetry(M, students)

    assert metrics["total_pairs"] == (20 * 19) // 2
    assert metrics["asymmetry_ratio"] > 0.5  # Đa số cặp phải có điểm chéo bất đối xứng
    assert metrics["mean_diff"] > 0.0
