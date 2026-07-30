vacant_seats = int(input("Enter the total number of seats vacant: "))
seats = int(input("Enter the number of seats required: "))
if vacant_seats>=seats:
    print("Booking Confirmed")
else:
    print("House Full")