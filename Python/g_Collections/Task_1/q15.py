def student_marks():
    students = {
        "Arun": 85,
        "Bobby": 90,
        "Charlie": 78
    }
    print(students)
    students["Manu"] = 87
    print("After adding new student: ",students)
    students["Bob"] = 94
    print("After updating marks for an existing student: ",students)
    for i in students:
        if students[i]>80:
            print(i,"scored above 80")

student_marks()