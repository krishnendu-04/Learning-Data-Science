m1 = float(input("Enter marks for 1st subject: "))
m2 = float(input("Enter marks for 2nd subject: "))
m3 = float(input("Enter marks for 3rd subject: "))
m4 = float(input("Enter marks for 4th subject: "))
m5 = float(input("Enter marks for 5th subject: "))
per = ((m1+m2+m3+m4+m5)/500)*100

if per>=75:
    print("Distinction")
elif per>=60:
    print("First Class")
elif per>=50:
    print("Second Class")
elif per>=40:
    print("Pass")
else:
    print("Fail")