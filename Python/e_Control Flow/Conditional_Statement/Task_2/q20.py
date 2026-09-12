rooms_available = int(input("Enter the total number of rooms available: "))
booking = int(input("Enter the number of rooms to book: "))
if rooms_available>=booking:
    print("Booking Confirmed")
else:
    print("Booking not confirmed. No adequate number of rooms available.")