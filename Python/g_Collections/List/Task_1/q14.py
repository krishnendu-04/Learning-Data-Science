marks = [23,67,34,28,90,76,43,98,73,12,66,84]
passed = 0
above_75 = 0 
for mark in marks:
    if mark>=40:
        passed+=1
    if mark>75:
        above_75+=1
print("Number of students who passed the exam: ",passed)
print("Number of students who scored above 75: ",above_75)