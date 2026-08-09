n = int(input("Enter the total number of deliveries: "))
for i in range(1,n+1):
    weight = float(input("Enter the weight of the package in kg: "))
    if weight>10:
        print("Package ID: P00"+str(i))