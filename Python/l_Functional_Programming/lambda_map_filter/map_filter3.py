lst = [55,69,40,24,12,87,45,33,9,68]
# lst1 = list(filter(lambda num:num%2!=0,lst))
# lst2 = list(map(lambda x:x**2,lst1))
lst1 = list(map(lambda x:x**2,filter(lambda num:num%2!=0,lst)))
print(lst1)