n = int(input("Enter the total number of departments: "))
for i in range(1,n+1):
    attendance = int(input("Enter the attendance of the department: "))
    if attendance<50:
        print("Department No: ",i)