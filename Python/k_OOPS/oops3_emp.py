class Employee:
    def setvalue(self,id,fname,lname,designation,salary,company):
        self.id = id
        self.fname = id
        self.fname = fname
        self.lname = lname
        self.designation = designation
        self.salary = salary
        self.company = company
    def printvalue(self):
        print(self.id,self.fname,self.lname,self.designation,self.salary,self.company)

emp1 = Employee()
emp1.setvalue(101,"Hana","Hussain","Project Manager",50000,"Wipro")
emp1.printvalue()

emp2 = Employee()
emp2.setvalue(108,"Gayathri","V","Accountant",48000,"EY")
emp2.printvalue()

emp3 = Employee()
emp3.setvalue(104,"Karthika","Falgunan","HR",64000,"KPMG")
emp3.printvalue()

emp4 = Employee()
emp4.setvalue(156,"Anamika","Babu","Engineer",70000,"Wipro")
emp4.printvalue()

emp5 = Employee()
emp5.setvalue(130,"Vedika","Deepak","Architect",86000,"Sthapathi")
emp5.printvalue()