available_seats = int(input("Enter the number of available seats: "))
seats = int(input("Enter the required number of seats: "))
if available_seats>=seats:
    print("Seats Reserved")
else:
    print("No enough seats available")