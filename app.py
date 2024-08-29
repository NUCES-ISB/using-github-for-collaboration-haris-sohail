# A fully funcitioning calculator app
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Undefined"
    
    return x / y

def mod(x, y):
    if(y == 0):
        return "Undefined"
    
    return x % y