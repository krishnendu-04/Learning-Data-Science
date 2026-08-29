marks = []
for i in range(5):
    marks.append(int(input("Enter the mark of the student: ")))
print("Mark of first student: ",marks[0])
print("Marks of last student: ",marks[-1])
print("Highest marks: ",max(marks))