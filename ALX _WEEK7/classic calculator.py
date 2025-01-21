class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #Method for addition
    """This method is to be used for addition"""
    def addition(self):
        try:
            return self.x + self.y
        except TypeError:
            print("Invalid input. Enter an integer!")


    #Method for subtraction
    """Method for subtraction"""
    def subtract(self):
        try:
            return self.x - self.y
        except TypeError:
            print("Invalid Input. Enter an integer!")

    """Method for multiplication"""
    def multiplication(self):
        try:
            return self.x * self.y
        except TypeError:
            print("Invalid Input. Enter an integer!")

    """Method for division"""
    def division(self):
        try:
            if self.y == 0:
                raise ZeroDivisionError("Cannot divide by zero!")
            return self.x / self.y

        except TypeError:
            print("Invalid input. Enter an integer")




add = Calculator(4, 4)
print(add.addition())
print("")

difference = Calculator(3, 6)
print(difference.subtract())
print("")

product = Calculator(2, 5)
print(product.multiplication())
print("")

divided = Calculator(8, 3)
print(divided.division())
print("")



