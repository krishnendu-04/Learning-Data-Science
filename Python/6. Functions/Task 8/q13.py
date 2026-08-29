def bp_analyser(patient_name, systolic, diastolic):
    if systolic < 120 and diastolic < 80:
        cat = "Normal"
        act = "Maintain healthy habits."
    elif 120 <= systolic <= 129 and diastolic < 80:
        cat = "Elevated"
        act = "Adopt lifestyle changes."
    elif (130 <= systolic <= 139) or (80 <= diastolic <= 89):
        cat = "High Stage 1"
        act = "Consult your doctor."
    elif systolic >= 140 or diastolic >= 90:
        cat = "High Stage 2"
        act = "Schedule a doctor's visit."
    elif systolic > 180 or diastolic > 120:
        cat = "Crisis"
        act = "Seek immediate medical attention."
    print("Patient Name: ",patient_name)
    print("Systolic reading: ",systolic)
    print("Diastolic reading: ",diastolic)
    print("Risk Category: ",cat)
    print(act)

name = input("Enter the name of the patient: ")
systolic = float(input("Enter the systolic value: "))
diastolic = float(input("Enter the diastolic value: "))
bp_analyser(name, systolic, diastolic)