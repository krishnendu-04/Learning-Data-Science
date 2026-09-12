lst = [10,10,45,65,45,89,32,23,32,"ML","DL","ML"]
lst1 = []
for i in lst:
    if i not in lst1:
        lst1.append(i)
print(lst1)