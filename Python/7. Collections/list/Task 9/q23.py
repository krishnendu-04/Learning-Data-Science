student_marks = [85, 90, 78, 93, 88, 76, 95, 89, 84, 91, 79, 88, 93, 80, 86]
print(student_marks)
print("Students with same marks: ")
for i in range(len(student_marks)):
    for j in range(i+1,len(student_marks)):
        if student_marks[i]==student_marks[j]:
            print("Student",i+1,"and",j+1)
student_marks.sort()
print("Top 5 marks: ",student_marks[-5:])
print("Second highest mark: ",student_marks[-2])