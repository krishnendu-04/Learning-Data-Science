n = int(input("Enter the number of locations: "))
for i in range(1,n+1):
    signal = float(input("Enter the signal strength: "))
    if signal<30:
        print("Location ID: L00"+str(i))