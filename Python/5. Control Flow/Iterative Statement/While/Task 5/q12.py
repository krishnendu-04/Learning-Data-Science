total = 0
deposit = float(input("Enter the deposit amount: "))
while deposit!=0:
    total+=deposit
    deposit = float(input("Enter the deposit amount: "))
print("Final balance",total)