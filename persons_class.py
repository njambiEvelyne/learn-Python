class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def __str__(self):
        return f"Robot(name = {self.name}, color= {self.color}, weight = {self.weight})"



r1 = Robot("Tom", "red", 30)
print(r1)
print("")

r2 = Robot("Emmy", "blue", 40)
print(r2)
print('')

class Person:
    def __init__(self, name, personality, is_sitting, r):
        self.name = name
        self.personality = personality
        self.isSitting = is_sitting
        self.robot_owned = r

    def sit_down(self):
        self.isSitting = True

    def stand_up(self):
        self.isSitting = False

    def __str__(self):
        return f"(Person name:{self.name} owns {self.robot_owned})"

p1 = Person("Evelyne","Quiet", False,r2 )
p2 = Person("Alice", "Talkative", True, r1)
print(p1)
print("")

print(p2)


