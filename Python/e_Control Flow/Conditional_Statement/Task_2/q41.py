water = int(input("Enter the current water level: "))
min_water_level = int(input("Enter the min water level required: "))
if water<min_water_level:
    print("Motor turned ON")
else:
    print("Motor turned OFF")