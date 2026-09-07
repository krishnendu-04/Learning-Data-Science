file = open("r4.txt","r")
lst = []
odd = []
even = []
for i in file:
    lst.append(int(i))
    if int(i)%2==0:
        even.append(int(i))
    else:
        odd.append(int(i))
print(lst)
print(even)
print(odd)
print("Sum of List 1: ",sum(lst))
print("Sum of Even numbers List: ",sum(even))
print("Sum of Odd numbers List: ",sum(odd))