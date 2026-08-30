ages = [67,23,12,42,56,78,90,30,27,8,17,68,58]
print(ages)
count_child = 0
count_senior = 0
for age in ages:
    if age<18:
        count_child+=1
    elif age>60:
        count_senior+=1
print("Number of children: ",count_child)
print("Number of senior citizens: ",count_senior)