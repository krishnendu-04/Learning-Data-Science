list1 = [10,11,10,87,11,67,45,78,45,45,78]
dict1 = {}
for num in list1:
    if num not in dict1:
        dict1[num] = 1
    else:
        dict1[num]+=1
print(dict1)