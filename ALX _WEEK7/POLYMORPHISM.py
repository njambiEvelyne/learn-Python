#Polymorphsim allows objects to take on
# different forms or behaviours based on
# their specific class of context
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 0.314 * self.radius **2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side **2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

