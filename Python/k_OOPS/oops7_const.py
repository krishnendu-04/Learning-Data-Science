class Student:
    def __init__(self,name,rollno,age):
        self.name = name
        self.rollno = rollno
        self.age = age

    def printvalue(self):
        print(self.name,self.rollno,self.age)

stud1 = Student("Ajay",23,21)
stud1.printvalue()

stud2 = Student("Ammu",21,23)
stud2.printvalue()