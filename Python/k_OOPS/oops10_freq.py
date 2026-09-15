class Employee:
    count = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.count+=1

    def printvalue(self):
        print(self.name,self.salary)

emp1 = Employee("Rohan",67000)
emp2 = Employee("Mohan",68000)
emp3 = Employee("Raj",56000)
emp4 = Employee("Hana",25000)
emp1.printvalue()
emp2.printvalue()
emp3.printvalue()
emp4.printvalue()
print("Employee Count: ",Employee.count)