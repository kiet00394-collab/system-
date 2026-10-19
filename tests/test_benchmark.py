import time
from matching import gale_shapley, count_blocking_pairs, make_random_prefs, run_benchmark
from data_io import generate_students
from scoring import compute_score_matrix, build_pref_lists

def test_nfr01_gale_shapley_200_students():
    """
    Kiểm tra NFR-01 (Bước A6): Thời gian ghép 200 sinh viên (100 A + 100 B) phải < 5 giây.
    """
    pa, pb = make_random_prefs(100, seed=42)
    t0 = time.perf_counter()
    match = gale_shapley(pa, pb)
    elapsed = time.perf_counter() - t0

    assert len(match) == 100
    assert elapsed < 5.0, f"Vi phạm NFR-01: Mất {elapsed:.4f}s (>= 5s)"
    assert count_blocking_pairs(match, pa, pb) == 0

def test_nfr01_end_to_end_200_students():
    """
    Kiểm tra toàn bộ luồng (Sinh dữ liệu -> Tính ma trận điểm -> Ghép phòng) cho 200 sinh viên < 5 giây.
    """
    t0 = time.perf_counter()
    students = generate_students(200, seed=42)
    M = compute_score_matrix(students)
    pa, pb = build_pref_lists(M, students)
    match = gale_shapley(pa, pb)
    elapsed = time.perf_counter() - t0

    assert len(match) == 100
    assert elapsed < 5.0, f"Toàn bộ luồng 200 SV quá chậm: {elapsed:.4f}s"
    assert count_blocking_pairs(match, pa, pb) == 0

def test_stress_1000_students_algorithm():
    """
    Stress test thuật toán Gale-Shapley với 1000 sinh viên (500 A + 500 B).
    """
    res = run_benchmark(student_totals=[100, 200, 1000], seeds=2)
    assert res[200] < 5.0
    assert res[1000] < 5.0