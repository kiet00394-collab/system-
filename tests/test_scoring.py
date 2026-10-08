import numpy as np
from models import Student
from data_io import generate_students
from scoring import criterion_sims, pair_score, compute_score_matrix, build_pref_lists

def test_identical_students_score_100():
    s1 = Student(0, "An", "A", 22.0, 7.0, 4, "phong", 2, 0, 1, {"game", "nhac"}, "sleep")
    s2 = Student(1, "Bình", "B", 22.0, 7.0, 4, "phong", 2, 0, 1, {"game", "nhac"}, "sleep")

    score = pair_score(s1, s2)
    assert score == 100.0, f"Expected 100.0, got {score}"

def test_different_students_score_asymmetry():
    s1 = Student(0, "An", "A", 22.0, 7.0, 5, "phong", 1, 0, 1, {"game"}, "tidy")
    s2 = Student(1, "Bình", "B", 22.0, 7.0, 4, "phong", 1, 0, 1, {"game"}, "smoke")

    score_12 = pair_score(s1, s2)
    score_21 = pair_score(s2, s1)

    assert 0.0 <= score_12 <= 100.0
    assert 0.0 <= score_21 <= 100.0
    assert score_12 != score_21

def test_compute_score_matrix_and_pref_lists():
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
        # Verify descending order of scores
        scores = [M[a][b] for b in lst]
        assert scores == sorted(scores, reverse=True)

    for b, lst in pref_b.items():
        assert set(lst) == set(ids_a)
        scores = [M[b][a] for a in lst]
        assert scores == sorted(scores, reverse=True)
