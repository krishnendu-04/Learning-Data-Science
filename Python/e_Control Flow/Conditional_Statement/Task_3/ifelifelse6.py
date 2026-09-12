age = int(input("Enter the age of the person: "))
if 0<=age<5:
    print("Free Ticket")
elif 5<=age<=12:
    print("Pay Rs.100")
elif 13<=age<=59:
    print("Pay Rs.200")
elif age>=60:
    print("Pay Rs.120")
else:
    print("Invalid age")