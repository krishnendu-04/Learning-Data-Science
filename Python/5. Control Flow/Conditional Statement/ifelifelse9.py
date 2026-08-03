yoe = int(input("Enter the employees years of experience: "))
if yoe<2:
    print("No Bonus")
elif 2<=yoe<=5:
    print("Rs.5000 Bonus")
elif 6<=yoe<=10:
    print("Rs.10000 Bonus")
elif yoe>10:
    print("Rs.20000 Bonus")
else:
    print("Invalid Years of Experience")