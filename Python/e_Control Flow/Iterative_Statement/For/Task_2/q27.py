n = int(input("Enter the number of patients: "))
for i in range(1,n+1):
    bmi = float(input("Enter the BMI of the patient: "))
    if bmi>=30:
        print("Patient P00"+str(i)+" is obese.")