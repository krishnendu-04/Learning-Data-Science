booked = ("A001","A002","A003","A004","A006","A010","A0011","A012")
print(booked)
check = input("Enter the seat number to check: ")
if check in booked:
    print("Seat already booked")
else:
    print("Seat not booked")