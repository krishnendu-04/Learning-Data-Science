class Bank:
    bank_name = "SBI"
    def setvalue(self,acc_no,name,balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
    def printvalue(self):
        print(self.acc_no,self.name,self.balance,Bank.bank_name)

b1 = Bank()
b1.setvalue("ACC987487398","Savitha",67000)
b1.printvalue()

b2 = Bank()
b2.setvalue("ACC738943927","Rajisha",90000)
b2.printvalue()

b3 = Bank()
b3.setvalue("ACC356365167","Irene",59000)
b3.printvalue()