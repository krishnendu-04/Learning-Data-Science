balance = float(input("Enter the account balance: "))
withdraw = input("Enter the withdrawal amount: ")
while balance>0 and withdraw!='stop':
    if float(withdraw)>balance:
        print("Can't withdraw amount greater than balance, Enter valid amount")
        withdraw = input("Enter the withdrawal amount: ")
        continue
    balance-=float(withdraw)
    print(balance)
    if balance>0:
        withdraw = input("Enter the withdrawal amount: ")