total_weight = int(input("Enter the total weight: "))
lift_capacity = int(input("Enter the lift's capacity: "))
if total_weight<lift_capacity:
    print("Lift Movement Allowed")
else:
    print("Overload")