def taxi_fare(distance_km, wait_minutes, hour):
    base_fare = 50
    print("Base Fare: ",base_fare)
    distance_fee = distance_km * 12
    print("Distance Fare: ",distance_fee)
    waiting_fee = wait_minutes * 2
    print("Waiting Fare: ",waiting_fee)
    total = base_fare + distance_fee + waiting_fee
    if hour<6 or hour>=22:
        night_fare = total * 1.25
        print("Night Fare: ",night_fare)
        total+=night_fare
    print("Total Fare: ",total)
    

distance_km = float(input("Enter the distance to be covered: "))
wait_minutes = int(input("Enter the waiting time in minutes: "))
hour = int(input("Enter the time of travel in hours (0-24hr clock): "))
taxi_fare(distance_km, wait_minutes, hour)