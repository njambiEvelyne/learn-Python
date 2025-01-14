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

r3 = Robot("evelyne", "white", 47)
print(r3)

