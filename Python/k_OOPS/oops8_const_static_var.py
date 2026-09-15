class Employee:
    company = "Infosys"
    designation = "Systems Engineer"
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    def printvalue(self):
        print(self.name,self.age,self.salary,Employee.company,Employee.designation)

emp1 = Employee("Pavi",21,34000)
emp1.printvalue()

emp2 = Employee("Riya",24,40000)
emp2.printvalue()