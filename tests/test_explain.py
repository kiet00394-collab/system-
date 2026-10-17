import pytest
from models import Student
from explain import explain_pair

def test_explain_pair_identical_students():
    s1 = Student(id=0, name="An", group="A", sleep=22.0, wake=7.0, tidy=5, study="phong",
                 noise=2, smoke=0, guests=2, hobbies={"game", "nhac"}, top="sleep")
    s2 = Student(id=1, name="Binh", group="B", sleep=22.0, wake=7.0, tidy=5, study="phong",
                 noise=2, smoke=0, guests=2, hobbies={"game", "nhac"}, top="sleep")
    explanation = explain_pair(s1, s2)
    assert "Trùng khớp:" in explanation
    assert "giờ đi ngủ" in explanation
    assert "mức gọn gàng" in explanation
    assert "Cần lưu ý:" not in explanation

def test_explain_pair_opposite_students():
    s1 = Student(id=0, name="An", group="A", sleep=21.0, wake=5.0, tidy=5, study="phong",
                 noise=1, smoke=0, guests=1, hobbies={"doc sach"}, top="sleep")
    s2 = Student(id=1, name="Binh", group="B", sleep=26.0, wake=10.0, tidy=1, study="thuvien",
                 noise=5, smoke=1, guests=5, hobbies={"game"}, top="smoke")
    explanation = explain_pair(s1, s2)
    assert "Cần lưu ý:" in explanation
    assert "giờ đi ngủ" in explanation or "hút thuốc" in explanation
