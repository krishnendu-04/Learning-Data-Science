from abc import abstractmethod,ABC

class Vehicle(ABC):
    @abstractmethod
    def start(key):
        pass

class Car(Vehicle):
    def start(self):
        print("Car start with key")

class Bike(Vehicle):
    def start(self):
        print("Bike start with key")

c = Car()
b = Bike()

c.start()
b.start()