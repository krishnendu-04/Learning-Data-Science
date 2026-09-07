file = open("r3.txt",'r')
numbers = []
for i in file:
    numbers.append(int(i))
print("Sum: ",sum(numbers))

"""for i in file:
    numbers.append(i.rstrip("\n"))
lstrip() ----> strips off from left
rstrip() ----> strips off from right"""