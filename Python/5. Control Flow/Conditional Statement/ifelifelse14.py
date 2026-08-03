weight = float(input("Enter the parcel weight in kg: "))
if weight<1:
    print("Rs.50")
elif 1<=weight<5:
    print("Rs.100")
elif 5<=weight<10:
    print("Rs.200")
elif weight>=10:
    print("Rs.400")