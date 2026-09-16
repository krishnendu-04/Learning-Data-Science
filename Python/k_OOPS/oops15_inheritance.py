class Animal:
    def eat(self):
        print("Eating...")

class Dog(Animal):
    def sound(self):
        print("Barking...")

d = Dog()
d.sound()
d.eat()