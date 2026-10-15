import pytest
from data_io import load_students_csv
from models import Student
from scoring import compute_score_matrix, build_pref_lists

def test_missing_columns_raises_value_error():
    """Kiểm tra file thiếu cột bắt buộc phải báo lỗi ValueError rõ ràng (NFR-04)."""
    with pytest.raises(ValueError) as excinfo:
        load_students_csv("data/error_missing_cols.csv")
    assert "Thiếu các cột bắt buộc" in str(excinfo.value)

def test_invalid_data_types_raises_value_error():
    """Kiểm tra file chứa kiểu dữ liệu sai (chữ thay vì số) phải báo lỗi có dòng cụ thể."""
    with pytest.raises(ValueError) as excinfo:
        load_students_csv("data/error_invalid_types.csv")
    assert "phải là số thực" in str(excinfo.value) or "phải là số nguyên" in str(excinfo.value)

def test_empty_file_raises_value_error():
    """Kiểm tra file CSV rỗng không có dữ liệu phải báo lỗi."""
    with pytest.raises(ValueError) as excinfo:
        load_students_csv("data/error_empty.csv")
    assert "File CSV rỗng" in str(excinfo.value)

def test_asymmetric_group_counts():
    """
    Kiểm tra xử lý khi số lượng sinh viên nhóm A và B không bằng nhau (lệch sĩ số).
    Hệ thống vẫn phải tính được ma trận điểm và danh sách ưu tiên bình thường.
    """
    students = [
        Student(0, "A1", "A", 22.0, 7.0, 4, "phong", 2, 0, 1, {"game"}, "sleep"),
        Student(1, "A2", "A", 23.0, 7.5, 3, "thuvien", 3, 0, 2, {"nhac"}, "tidy"),
        Student(2, "A3", "A", 21.5, 6.5, 5, "it", 1, 0, 1, {"doc sach"}, "noise"),
        Student(3, "B1", "B", 24.0, 8.0, 2, "phong", 4, 1, 3, {"game"}, "smoke"),
    ]  # 3 nhóm A, 1 nhóm B
    
    M = compute_score_matrix(students)
    assert M.shape == (4, 4)
    
    pref_a, pref_b = build_pref_lists(M, students)
    # Nhóm A có 3 người, mỗi người có danh sách ưu tiên gồm 1 người nhóm B (ID 3)
    assert len(pref_a) == 3
    for a_id in [0, 1, 2]:
        assert pref_a[a_id] == [3]
        
    # Nhóm B có 1 người, danh sách ưu tiên gồm cả 3 người nhóm A xếp theo thứ tự điểm giảm dần
    assert len(pref_b) == 1
    assert set(pref_b[3]) == {0, 1, 2}
    scores_for_b = [M[3][a] for a in pref_b[3]]
    assert scores_for_b == sorted(scores_for_b, reverse=True)
