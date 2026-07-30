bank_total = float(input("Enter the total amount in the account: "))
withdraw = float(input("Enter the amount to withdraw: "))
bank_total-=withdraw
if(bank_total>=1000):
    print("Withdrawal Allowed")
else:
    print("Withdrawal not allowed")