from app import *

def test_add():
    assert add(1, 2) == 3
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    
def test_subtract():
    assert subtract(1, 2) == -1
    assert subtract(0, 0) == 0
    assert subtract(-1, 1) == -2
    
def test_multiply():
    assert multiply(1, 2) == 2
    assert multiply(0, 0) == 0
    assert multiply(-1, 1) == -1
    
def test_divide():
    assert divide(1, 2) == 0.5
    assert divide(0, 0) == "Undefined"
    assert divide(-1, 1) == -1
    
def test_mod():
    assert mod(1, 2) == 1
    assert mod(0, 0) == "Undefined"
    assert mod(-1, 1) == 0
    
# Run the tests
test_add()
test_subtract()
test_multiply()
test_divide()