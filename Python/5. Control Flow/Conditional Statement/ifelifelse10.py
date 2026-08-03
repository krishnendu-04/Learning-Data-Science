bmi = float(input("Enter the BMI Value: "))
if bmi<18.5:
    print("Underweight")
elif 18.5<=bmi<=24.9:
    print("Normal Weight")
elif 25<=bmi<=29.9:
    print("Overweight")
elif bmi>=30:
    print("Obese")
else:
    print("Invalid BMI")