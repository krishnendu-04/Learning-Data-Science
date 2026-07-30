bank_total = int(input("Enter the total amount in the account: "))
withdraw = int(input("Enter the amount to withdraw: "))
bank_total-=withdraw
if(bank_total>=1000):
    print("Withdrawal Allowed")
else:
    print("Withdrawal not allowed")