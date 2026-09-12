acc_bal = float(input("Enter the account balance: "))
withdraw = float(input("Enter the withdrawal amount: "))
if acc_bal>=withdraw:
    print("Withdrawal Successful! ")
elif acc_bal<withdraw:
    print("Insufficient Balance")
else:
    print("Invalid Amount")