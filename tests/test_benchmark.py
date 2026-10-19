import pytest
import time
from data_io import generate_mock_students
from models import MatchingConfig
from scoring import build_preference_lists
from matching import gale_shapley

def test_nfr01_performance_200_students():
    """
    Kiểm tra tiêu chí NFR-01: Thuật toán phải ghép xong 200 sinh viên dưới 5 giây.
    """
    config = MatchingConfig()
    students = generate_mock_students(200, seed=42)
    
    start_time = time.perf_counter()
    pa, pb = build_preference_lists(students, config)
    match, _ = gale_shapley(students, pa, pb)
    execution_time = time.perf_counter() - start_time
    
    print(f"\n[NFR-01] Thoi gian thuc hien cho 200 sinh vien: {execution_time:.4f}s")
    assert execution_time < 5.0, f"Vi pham NFR-01: Thoi gian chay {execution_time:.2f}s >= 5.0s"

def test_stress_1000_students():
    """
    Kiểm tra khả năng chịu tải (Stress test) với 1000 sinh viên.
    """
    config = MatchingConfig()
    students = generate_mock_students(1000, seed=100)
    
    start_time = time.perf_counter()
    pa, pb = build_preference_lists(students, config)
    match, _ = gale_shapley(students, pa, pb)
    execution_time = time.perf_counter() - start_time
    
    print(f"\n[Stress Test] Thoi gian thuc hien cho 1000 sinh vien: {execution_time:.4f}s")
    assert execution_time < 15.0, "Thuật toán xử lý quá chậm với 1000 sinh viên"