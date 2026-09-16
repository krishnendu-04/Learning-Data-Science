class UPI:
    def pay(self):
        print("Pay via UPI ID")

class Card:
    def pay(self):
        print("Pay via Debit/Credit Card")

class Cash:
    def pay(self):
        print("Pay with Cash")

cust1 = UPI()
cust2 = Card()
cust3 = Cash()

cust1.pay()
cust2.pay()
cust3.pay()