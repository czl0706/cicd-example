import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from example import add, subtract

def test_add():
    assert add(3, 4) == 7
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(0, 0) == 0
