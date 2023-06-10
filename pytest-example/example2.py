from pytest import approx

def add(a, b):
    return a + b

def test_add():
    result = add(0.1, 0.2)
    assert abs(result - 0.3) < 1.0e-7