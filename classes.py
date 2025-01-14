class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

#Inheritance
class Lion(Animal):
    def speak(self):
        return  f"{self.name} the lion roars"
zoo = [
    Lion ("Simba")
]
for animal in zoo:
    print(f"{animal.speak()}")
