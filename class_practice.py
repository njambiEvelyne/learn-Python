class Person:
    def __init__(self, name, age, career):
        self.name = name
        self.age = age
        self.career = career

    def __str__(self):
        return f"{self.name} is {self.age} years old.{self.name} works as a {self.career}"

doctor = Person("Rose", 17, "Orthopaedics doctor")
print(doctor)
print("")

soldier = Person("Kane", 34, "soldier")
print(soldier)
print("")


