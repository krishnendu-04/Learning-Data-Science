marks = [85,12,90,38,78,26,92]
print(marks)
for i in marks:
    if i<40:
        marks.remove(i)
print("Students who passed: ",marks)