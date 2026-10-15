import time
from data_io import generate_students
from scoring import compute_score_matrix

def test_score_matrix_performance_nfr01():
    """Kiểm tra thời gian tính toán ma trận điểm cho 200 sinh viên phải dưới 1 giây (NFR-01)."""
    students = generate_students(200, seed=42)
    start_time = time.perf_counter()
    M = compute_score_matrix(students)
    duration = time.perf_counter() - start_time
    
    assert M.shape == (200, 200)
    assert duration < 2.0, f"Thời gian tính toán quá lâu: {duration:.4f}s"
