passed = 0
marks = int(input("Enter the marks of the student: "))
if marks>=40:
    passed+=1
while(marks!=-1):
    marks = int(input("Enter the marks of the student: "))
    if marks>=40:
        passed+=1
print(passed)