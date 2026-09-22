lst = [1,2,2,3,3,3,7,8,7,4]
#count the number of numbers
# lst1 = [(i,lst.count(i)) for i in set(lst)]
# print(lst1)

dict1 = {i:lst.count(i) for i in lst}
print(dict1)