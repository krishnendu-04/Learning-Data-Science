n = int(input("Enter the total number of students: "))
for i in range(1,n+1):
    note = int(input("Enter the number of notebooks received: "))
    if note<3:
        print("Student ID: S00"+str(i))