numbers = [1, 2, 2, 3, 4, 4, 5]
set1 = set()
lst = [i for i in numbers if not(i in set1 or set1.add(i))]
print(lst)