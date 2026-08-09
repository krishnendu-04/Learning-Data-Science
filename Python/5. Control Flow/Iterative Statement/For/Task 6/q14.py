n = int(input("Enter the number of items in repair: "))
for i in range(1,n+1):
    charge = float(input("Enter the repair charge: "))
    if charge>5000:
        print("Repair ID: R00"+str(i))
        