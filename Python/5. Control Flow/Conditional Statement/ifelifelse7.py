units = int(input("Enter the units consumed: "))
if 0<=units<=100:
    print("Total Electricity Bill (Rs.3 per unit) : ",3*units)
elif 101<=units<=200:
    print("Total Electricity Bill (Rs.5 per unit) : ",5*units)
elif 201<=units<=500:
    print("Total Electricity Bill (Rs.7 per unit) : ",7*units)
elif units>500:
    print("Total Electricity Bill (Rs.10 per unit) : ",10*units)
else:
    print("Invalid input")