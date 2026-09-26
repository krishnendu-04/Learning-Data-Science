names = ['Amit', 'Bala', 'Chitra']
marks = [85, 40, 92]
names_marks = [names[i] for i in range(len(names)) if marks[i]>50]
print(names_marks)