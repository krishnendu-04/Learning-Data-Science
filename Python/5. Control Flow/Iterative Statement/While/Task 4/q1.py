acc_bal = 0
deposit = float(input("Enter the deposit money: "))
while(deposit!=0):
    acc_bal+=deposit
    deposit = float(input("Enter the deposit money: "))
print("Final Balance is",acc_bal)