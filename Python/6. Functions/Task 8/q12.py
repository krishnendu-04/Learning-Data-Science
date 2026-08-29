def diet_plan(gender, weight_kg, height_cm, age, activity):
    inches = height_cm / 2.54
    if gender:
        ideal_weight = 45.5 + 2.3 * (inches - 60)
        BMR  = 447.6 + (9.2 * weight_kg) + (3.1 * height_cm - 4.3 * age)
    else:
        ideal_weight = 50 + 2.3 * (inches - 60)
        BMR = 88.36 + (13.4 * weight_kg) + (4.8 * height_cm - 5.7 * age)
    if activity==1:
        cal_need = BMR * 1.2
    elif activity==2:
        cal_need = BMR * 1.375
    elif activity==3:
        cal_need = BMR * 1.55
    else:
        print("Invalid activity choice")
        return
    print("Ideal Weight: ",ideal_weight)
    print("BMR: ",BMR)
    print("Daily Calorie Target: ",cal_need)



gender = input("Enter F if you're female, else enter M: ").upper() == "F"
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))
age = int(input("Enter your age: "))
activity = int(input("1. Sedentary\n2. Light\n3. Active\nEnter your activity(1-3): "))
diet_plan(gender, weight, height, age, activity)