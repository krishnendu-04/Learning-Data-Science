class Person:
    def setvalue(self,name,age,course,college,city):
        self.name = name
        self.age = age
        self.course = course
        self.college = college
        self.city = city
    def printvalue(self):
        print(self.name,self.age,self.course,self.college,self.city)

person1 = Person()
person1.setvalue("Parvathy",20,"DA","Abc","IJK")
person1.printvalue()