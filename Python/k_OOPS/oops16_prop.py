class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def display1(self):
        print(self.name,self.salary)

class Manager(Employee):
    def __init__(self,name,salary,dept):
        super().__init__(name,salary)
        self.dept = dept
    def display2(self):
        print(self.dept)

emp1 = Manager("Rajesh",67000,"DS")
emp1.display1()
emp1.display2()