attendance_status = ["P", "A", "P", "P", "A"]
present=0
absent=0
for i in attendance_status:
    if i=="P":
        present+=1
    else:
        absent+=1
print("Present: ",present)
print("Absent: ",absent)