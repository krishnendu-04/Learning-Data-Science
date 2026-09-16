from abc import abstractmethod,ABC

class Bank(ABC):
    @abstractmethod
    def interest(self):
        pass

class SBI(Bank):
    def interest(self):
        print(f"4% interest")

class ICICI(Bank):
    def interest(self):
        print(f"8% interest")

class HDFC(Bank):
    def interest(self):
        print(f"6% interest")

cust1 = SBI()
cust2 = ICICI()
cust3 = HDFC()

cust1.interest()
cust2.interest()
cust3.interest()