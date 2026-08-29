def parking_fee(vehicle_type, hours, lost_ticket=False):
    billable_hours = max(0, hours - 1)
    if lost_ticket:
        bill=500
    elif vehicle_type==1:
        bill=billable_hours*10
    elif vehicle_type==2:
        bill=billable_hours*30
    elif vehicle_type==3:
        bill=billable_hours*60

    print("Vehicle Type:", vehicle_type)
    print("Duration:", hours, "hours")
    print("Total Fee: ", bill)

vehicle = int(input("1. Two Wheeler Parking\n2. Car/SUV Parking\n3. Heavy Vehicle\nEnter your choice of vehicle(1-3): "))
hours = int(input("Enter the hours of parking needed: "))
lost_ticket = input("Enter True if ticket is lost,else enter False: ") == "True"
parking_fee(vehicle, hours, lost_ticket)