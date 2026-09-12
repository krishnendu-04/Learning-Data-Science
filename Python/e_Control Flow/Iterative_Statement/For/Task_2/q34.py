n = int(input("Enter the total number of students: "))
for i in range(1,n+1):
    course = input("Did you complete the course? (y/n): ")
    if course=='y' or course=='Y':
        print("Certificate Granted! \n Certificate No: C00"+str(i))