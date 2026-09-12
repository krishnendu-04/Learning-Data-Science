n = int(input("Enter the number of the month: "))
if 1<=n<=4:
    print("Summer")
elif 5<=n<=8:
    print("Rainy")
elif 9<=n<=12:
    print("Winter")
else:
    print("Invalid month")