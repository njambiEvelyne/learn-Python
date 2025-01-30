class Airplane:
    def fly(self):
        print("Airplane is flying")
class Bird:
    def fly(self):
        print("Bird is flying")
class Fish:
    def swim(self):
        print("Fish is swimming")
airplane = Airplane()
bird = Bird()
fish = Fish()

def fly_object(object):
    return object.fly()

fly_object(airplane)
fly_object(bird)
fly_object(fish)
