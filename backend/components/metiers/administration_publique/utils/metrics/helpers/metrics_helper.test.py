# metrics_helper.test.py
# Tests unitaires Python pour metrics_helper
from .metrics_helper import average

def test_average():
    assert average([1, 2, 3]) == 2

def test_average_empty():
    assert average([]) == 0
