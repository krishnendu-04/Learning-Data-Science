lst = [1,2,2,3,3,3,7,8,7,4]
#count the number of numbers
lst1 = [(i,lst.count(i)) for i in set(lst)]
print(lst1)
# dict1 = {}
# for i in lst:
#     if i not in dict1.keys():
#         dict1[i]=1
#     else:
#         dict1[i]+=1
# print(dict1)