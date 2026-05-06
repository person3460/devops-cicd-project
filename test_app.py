from app import add, subtract

def test_add():
    assert add(5, 3) == 8
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(5, 5) == 0

print("All tests passed!")
