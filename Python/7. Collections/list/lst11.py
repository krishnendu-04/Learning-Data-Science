lst = []
even_lst = []
odd_lst = []
for i in range(1,51):
    lst.append(i)
    if i%2==0:
        even_lst.append(i)
    else:
        odd_lst.append(i)
print("Sum of list: ",sum(lst))
print("Length of list: ",len(lst))

print("Sum of even list: ",sum(even_lst))
print("Length of even list: ",len(even_lst))

print("Sum of odd list: ",sum(odd_lst))
print("Length of odd list: ",len(odd_lst))
