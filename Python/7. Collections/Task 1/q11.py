def flight_details():
    flight_details = ("AI101", "Kochi", "Bengaluru", "08:00 AM")
    print(flight_details)
    for i in flight_details:
        print(i)
    print("Source: ",flight_details[1])
    print("Destination: ",flight_details[2])

flight_details()