def student_details():
    student = (101,"Lisa",12,"Maths","Computer","Chemistry","Physics")
    print(student)
    print(student[1])
    print("\nAll elements in the tuple: ")
    for i in range(len(student)):
        print(student[i])

student_details()