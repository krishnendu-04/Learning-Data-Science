student = {
    "Roll_no" : 19,
    "Name" : "Abhi",
    "Age" : 20,
    "Mark" :  78.5,
    "Course" : "Data Science"
}
print(student)
print()
for i in student:
    print(i)
print()
for i in student:
    print(i,":",student[i])
print("Roll_no" in student)