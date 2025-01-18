def add (x,y):
    """"
    Add function
    """
    return x + y

def subtract(a, b):
    """Subtract function"""
    return a - b

def multiply(x, y):
    """Multiplication function"""
    return x *y

def divide (x,y):
    """Division function"""
    try:
        return x / y
    except ZeroDivisionError:
        print("Cannot divide by zero")

    # if y == 0:
    #     raise ZeroDivisionError("Can't divide by zero")
    # return x/y


print(add(3,1))
print(divide(3,0))
