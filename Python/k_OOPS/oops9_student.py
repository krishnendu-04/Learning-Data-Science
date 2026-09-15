class Student:
    def __init__(self,name,rollno,mark1,mark2,mark3):
        self.name = name
        self.rollno = rollno
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
    def total(self):
        return self.mark1+self.mark2+self.mark3
    def average(self):
        return self.total()/3
    def printvalue(self):
        print(self.name,self.rollno,self.total(),self.average())

stud1 = Student("Riya",12,87,90,76)
stud1.printvalue()

stud1 = Student("Sarah",34,99,90,88)
stud1.printvalue()