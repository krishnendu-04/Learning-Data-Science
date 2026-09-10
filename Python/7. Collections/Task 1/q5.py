def patient_queue(names):
    for i in names:
        print(i)
    names.pop(0)
    print("After removal of first patient: ",names)
    names.append(input("Enter the name of the patient to be added: "))
    print("After adding a patient to the end of the list: ",names)
    search = input("Enter the patient to search for: ")
    if search in names:
        print("Patient in queue")
    else:
        print("Patient not in queue")

n = int(input("Enter the number of patients: "))
names = []
for i in range(n):
    names.append(input("Enter the name of the patient: "))
patient_queue(names)