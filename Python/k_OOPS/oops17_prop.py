class Car:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def printvalue(self):
        print(self.name,self.price)

class Brand(Car):
    def display(self):
        print(f"{self.name} is driving")

c1 = Brand("BMW",28000000)
c1.printvalue()
c1.display()