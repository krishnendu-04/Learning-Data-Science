n = int(input("Enter the total number of students: "))
for i in range(1,n+1):
    books = int(input("Enter the number of books read by student:"))
    if books>5:
        print("Student No",i)