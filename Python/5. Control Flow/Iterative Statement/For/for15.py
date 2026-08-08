present = 0
for i in range(5):
    attendance = input("Mark your attendance (P for Present,A for absent): ")
    if attendance=="P":
        present+=1
print("Number of students present: ",present)