bal = 10000
withdraw = float(input("Enter the withdrawal amount: "))
while(bal>0 and withdraw!=0):
    bal-=withdraw
    print("Bank Balance: ",bal)
    withdraw = float(input("Enter the withdrawal amount: "))
    if withdraw>=bal:
        print("Insufficient Bank Balance")
        break