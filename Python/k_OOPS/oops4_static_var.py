class Employee:
    company = "Infosys" #Static variable
    def setvalue(self,name,salary,designation):
        self.name = name
        self.salary = salary
        self.designation = designation
    def printvalue(self):
        print(self.name,self.salary,self.designation,Employee.company)

emp1 = Employee()
emp1.setvalue("Anurag",78000,"Engineer")
emp1.printvalue()