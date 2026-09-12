pos,neg,zero = 0,0,0
n = int(input("How many numbers to be checked? "))
for i in range(n):
    num = int(input("Enter the number: "))
    if num>0:
        pos+=1
    elif num<0:
        neg+=1
    else:
        zero+=1
print("Number of positive numbers is",pos)
print("Number of negative numbers is",neg)
print("Number of zeros is",zero)