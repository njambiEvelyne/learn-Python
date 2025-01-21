class Rectangle:
    def __init__(self, x, y):
        self.length = x
        self.breadth = y
    #This is a destructor
    def __del__(self):
        class_name = self.__class__.__name__
        print(f'Object with the dimensions {self.length}, and {self.breadth} has been destroyed...')

    def area(self):
        return self.length * self.breadth

#The main code
r1 = Rectangle(12, 13)
print(r1.area())

r2 = Rectangle(2,7 )
print(r2.area())

r3 = r1
print(r3.area())

del r1
del r2
del r3

