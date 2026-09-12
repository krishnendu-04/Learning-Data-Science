balance = 0
while balance<500:
    recharge = float(input("Enter the amount to be recharged: "))
    if balance+recharge>500:
        print("Total amount greater than 500, Enter valid amount")
        recharge = float(input("Enter the amount to be recharged: "))
    balance+=recharge
    print(balance)