from io import StringIO
from pathlib import Path

import pandas as pd
import pytest

from data_io import generate_students, load_students_csv
from scoring import build_pref_lists, compute_score_matrix


CSV_HEADER = "id,name,group,sleep,wake,tidy,study,noise,smoke,guests,hobbies,top"


def csv_row(student_id, name, group, sleep="22"):
    return f"{student_id},{name},{group},{sleep},7,3,phong,3,0,2,game,sleep"


def load_csv_rows(*rows):
    return load_students_csv(StringIO("\n".join([CSV_HEADER, *rows])))


def test_sample_csv_contains_twenty_balanced_students():
    sample_path = Path(__file__).resolve().parents[1] / "data" / "sample_students.csv"

    students = load_students_csv(sample_path)

    assert len(students) == 20
    assert sum(student.group == "A" for student in students) == 10
    assert sum(student.group == "B" for student in students) == 10


def test_csv_ids_are_normalized_for_matrix_indexing():
    students = load_csv_rows(
        csv_row(101, "An", "a"),
        csv_row(900, "Binh", "B", sleep="23"),
    )

    matrix = compute_score_matrix(students)
    pref_a, pref_b = build_pref_lists(matrix, students)

    assert [student.id for student in students] == [0, 1]
    assert list(pref_a) == [0]
    assert pref_a[0] == [1]
    assert pref_b[1] == [0]


def test_csv_with_unequal_groups_still_builds_preferences():
    students = load_csv_rows(
        csv_row(10, "An", "A"),
        csv_row(20, "Binh", "A", sleep="23"),
        csv_row(30, "Chi", "B", sleep="24"),
    )

    pref_a, pref_b = build_pref_lists(compute_score_matrix(students), students)

    assert pref_a == {0: [2], 1: [2]}
    assert set(pref_b) == {2}
    assert set(pref_b[2]) == {0, 1}


def test_load_students_csv_rejects_missing_columns():
    with pytest.raises(ValueError, match="Thiếu các cột bắt buộc"):
        load_students_csv(StringIO("id,name,group\n1,An,A\n"))


def test_load_students_csv_rejects_invalid_numeric_data():
    with pytest.raises(ValueError):
        load_csv_rows(csv_row(1, "An", "A", sleep="late"))


def test_load_students_csv_rejects_empty_file():
    with pytest.raises(pd.errors.EmptyDataError):
        load_students_csv(StringIO(""))


def test_generated_students_are_deterministic_and_balanced():
    first = generate_students(20, seed=42)
    second = generate_students(20, seed=42)

    assert first == second
    assert sum(student.group == "A" for student in first) == 10
    assert sum(student.group == "B" for student in first) == 10
