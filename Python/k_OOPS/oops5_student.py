class Student:
    college = "SCMS"
    def setvalue(self,rollno,name,age,mark):
        self.rollno = rollno
        self.name = name
        self.age = age
        self.mark = mark
    def printvalue(self):
        print(self.rollno,self.name,self.age,self.mark,Student.college)

stud1 = Student()
stud1.setvalue("SCM22CD016","Anu",23,98)
stud1.printvalue()

stud2 = Student()
stud2.setvalue("SCM22CD033","Fidha",22,100)
stud2.printvalue()

stud3 = Student()
stud3.setvalue("SCM22CD054","Parvathy",22,90)
stud3.printvalue()