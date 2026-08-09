n =int(input("Enter the number of students: "))
for i in range(1,n+1):
    status = input("Are you eligible for a scholarship? (y/n) : ")
    if status=="y" or status=='Y':
        print("Student Roll Number: ",i)