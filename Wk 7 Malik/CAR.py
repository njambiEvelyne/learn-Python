class Engine:
    def start(self):
        print("Engine started.")
class Car:
    def __init__(self, engine):
        self.engine = engine
    def move(self):
        print("Car is moving.")

engine = Engine()
car = Car(engine)
car.engine.start()