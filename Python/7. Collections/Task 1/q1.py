def analyze_marks(marks):
    high = marks[0]
    count = 0
    for i in marks:
        if i>high:
            high = i
        if i>75:
            count+=1
    print("Highest marks: ",high)
    print("Number of students who scored above 75: ",count)
    marks.sort()
    print("Marks in ascending order: ",marks)

marks=[]
n = int(input("Enter the number of students: "))
for i in range(n):
    marks.append(float(input("Enter the mark: ")))
analyze_marks(marks)