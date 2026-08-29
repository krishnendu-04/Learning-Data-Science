def calorie_burn(activity, weight_kg, duration_min):
    duration_hrs = duration_min / 60
    if activity==1:
        MET = 3.5
    elif activity==2:
        MET = 8.0
    elif activity==3:
        MET = 6.0
    elif activity==4:
        MET = 7.0
    elif activity==5:
        MET = 5.0
    else:
        print("Invalid Activity")
        return
    calories = MET * weight_kg * duration_hrs
    print("Calories burned: ",calories)
    print("You got this!!!!")


activity = int(input("1. Walking\n2. Running\n3. Cycling\n4. Swimming\n5. Weight Training\nEnter your activity(1-5): "))
weight_kg = float(input("Enter your weight in kg: "))
duration_min = int(input("Enter the duration of the activity in mins: "))
calorie_burn(activity, weight_kg, duration_min)