def attendance_report():
    attendance = {
        "Alice": 85.5,
        "Bob": 72.2,
        "Charlie": 92.0,
        "David": 67.8
    }
    print(attendance)
    count=0
    for i in attendance:
        if attendance[i]<75:
            print(i,"is not eligible")
        else:
            count+=1
    print("Eligible number of students: ",count)

attendance_report()