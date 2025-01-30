from datetime import date
#Instance method
class Calculator:
    def __init__(self, version:int):
        self.version = version
    def description(self):
        return f"Currently running Calculator on version: {self.version}"

    @staticmethod
    def add_numbers(self, *numbers :float):
        return sum(numbers)

calc1 = Calculator(10)
print(calc1.description())

calc2 = Calculator(200)
print(calc2.description())

print(Calculator.add_numbers(4, 30, 40))

#The class method
from datetime import date
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    def description(self):
        return f"{self.name} is {self.age} years old."

    @classmethod
    def age_from_year(cls, name:str, birth_year:int):
        current_year = date.today().year
        age: int = current_year - birth_year
        return cls(name, age)

if __name__== "__main__":
    evelyne = Person.age_from_year("Evelyne", 2005)
    print(evelyne.description())





