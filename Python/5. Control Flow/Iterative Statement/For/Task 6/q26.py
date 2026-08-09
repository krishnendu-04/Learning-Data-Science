n = int(input("Enter the total number of passengers: "))
for i in range(1,n+1):
    print("\nPassenger",i)
    weight_limit=float(input("Enter the weight limit: "))
    weight = float(input("Enter the weight: "))
    if weight>weight_limit:
        print("Passenger ID: P00"+str(i))