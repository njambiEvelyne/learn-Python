class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Generic animal sound."

class Dog(Animal):
    def make_sound(self):
        print("woof!")

lassie = Dog("Lassie")
print(lassie.make_sound())

