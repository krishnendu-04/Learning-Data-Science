def travel_calculator(distance_km, speed_kmph):
    time = distance_km/speed_kmph
    hrs = int(time)
    mins = (time-hrs)*60
    print("Distance: ",distance_km)
    print("Speed: ",speed_kmph)
    print("Estimated travel time: ",hrs,"hrs",int(mins),"mins")
    if speed_kmph>120:
        print("Overspeed Warning! ")

distance_km = float(input("Enter the distance covered by the vehicle in km: "))
speed_kmph = float(input("Enter the speed of the vehicle in kmph: "))
travel_calculator(distance_km, speed_kmph)