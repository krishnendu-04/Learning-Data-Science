def attendance(days):
    count=0
    for i in range(days):
        attendance = input("Enter P for presentence or A for absentence: ")
        if attendance=="P" or attendance=="p":
            count+=1
    return count
d = int(input("Enter the number of days: "))
present = attendance(d)
print("Present days: ",present)