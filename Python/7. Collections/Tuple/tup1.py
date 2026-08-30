tup = (100,200,300,400,500,600)
list1 = list(tup)
print(list1)
list1[2] = "hello"
print(list1)
tup = tuple(list1)
print(tup)