n = int(input("Enter the limit: "))
sum = 0
for i in range(1,n+1):
    if i%5==0:
        sum+=i
print("Sum of all numbers between 1 and",n,"is",sum)