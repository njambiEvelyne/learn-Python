class Bird:
    def fly(self):
        print("Flying in the sky.")

class Mammal:
    def run(self):
        print("Running in the ground.")


class Bat(Bird, Mammal):
    def fly(self):
        print("I am a bat, I can fly using echolocation.")

    def run(self):
        print("I can also run like a mammal.")

bat = Bat()
print(bat.fly())
print(bat.run())

