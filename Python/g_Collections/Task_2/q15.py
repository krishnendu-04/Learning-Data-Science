students = [
    ["Arya", 81],
    ["Adarsh", 88],
    ["Lakshmi", 96],
    ["Fathima", 99],
    ["Ananthu", 92],
    ["Rahul", 71],
    ["Midhun", 98]
]
print(students)
for i in range(len(students)):
    for j in range(0,len(students)-i-1):
        if students[j][1]<students[j+1][1]:
            students[j], students[j + 1] = students[j + 1], students[j]
print("After sorting: ",students)
print("Top 5 students: ")
for i in range(5):
    print(students[i][0])
      