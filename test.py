import pytest
from main import StudentsInMLOps

def test_enrollStudents():
    class_instance = StudentsInMLOps()
    class_instance.enrollStudents(5)
    assert class_instance.getTotalStrength() == 5

def test_dropStudents():
    class_instance = StudentsInMLOps()
    class_instance.enrollStudents(5)
    class_instance.dropStudents(2)
    assert class_instance.getTotalStrength() == 3

def test_getClassName():
    class_instance = StudentsInMLOps()
    assert class_instance.getClassName() == "StudentsInMLOps"
