lst1 = ["arya","malu","priya","hari","sree"]
lst2 = [100,45,67,89]
students ={}
for i in range(len(lst1)):
    if i<len(lst2):
        students[lst1[i]] = lst2[i]
    else:
        students[lst1[i]] = 0
print(students)