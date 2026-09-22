string = "in 1984 there were 13 instance of a protest with over 1000 people attending"
lst = string.split()
lst1 = [i for i in lst if i.isnumeric()]
print(lst1)
#get only number