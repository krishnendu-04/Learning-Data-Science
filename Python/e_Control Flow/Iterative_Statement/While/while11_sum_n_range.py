lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))
sum=0
while lower<=upper:
    sum+=lower
    lower+=1
print(sum)