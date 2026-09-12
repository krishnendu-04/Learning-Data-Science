def medication_reminder(med_name, last_dose_hour, interval_hrs,doses_remaining):
    print("Medicine Name: ",med_name)
    for i in range(1,doses_remaining+1):
        next_hour = (last_dose_hour + interval_hrs * i) % 24
        print("Dose",i,str(next_hour)+":00")

name = input("Enter the name of the medicine: ")
last_dose_hr = int(input("Enter the hour of the last dose: "))
interval_hrs = int(input("Enter the interval between doses: "))
doses_remaining = int(input("Enter the doses remaining: ")) 
medication_reminder(name, last_dose_hr, interval_hrs,doses_remaining)