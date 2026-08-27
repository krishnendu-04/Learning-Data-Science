def calculate_bmi(weight, height):
    return weight/(height**2)

h = float(input("Enter your height in meter: "))
w = float(input("Enter your weight in kgs: "))
bmi = calculate_bmi(w, h)
print(bmi)