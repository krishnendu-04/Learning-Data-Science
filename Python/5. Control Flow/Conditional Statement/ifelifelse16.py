age = int(input("Enter the age: "))
if age<5:
    print("Free Bus Ticket")
elif 5<=age<=18:
    print("Student Fare")
elif 18<age<=59:
    print("Full Fare")
elif age>=60:
    print("Senior Citizen Fare")