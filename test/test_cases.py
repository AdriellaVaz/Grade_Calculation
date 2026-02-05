import pytest
from src.app import calculate_average, calculate_grade


def test_student_A_plus():
    marks = [95, 90, 92, 94, 93]
    avg = calculate_average(marks)
    assert calculate_grade(avg) == "A+"


def test_student_A():
    marks = [80, 78, 75, 82, 77]
    avg = calculate_average(marks)
    assert calculate_grade(avg) == "A"


def test_student_B():
    marks = [65, 60, 62, 68, 64]
    avg = calculate_average(marks)
    assert calculate_grade(avg) == "B"


def test_student_C():
    marks = [55, 52, 50, 58, 54]
    avg = calculate_average(marks)
    assert calculate_grade(avg) == "C"


def test_student_fail():
    marks = [40, 45, 42, 38, 44]
    avg = calculate_average(marks)
    assert calculate_grade(avg) == "Fail"
