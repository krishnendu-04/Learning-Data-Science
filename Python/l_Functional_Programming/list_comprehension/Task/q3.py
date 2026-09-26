lst1 = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
lst2 = [i for lst in lst1 for i in lst]
print(lst1)
print(lst2)