n = int(input("Enter the limit: "))
i = 2
sum = 0
while i<=n:
    sum+=i
    i+=2
print("Sum of even numbers is",sum)

'''
while i<=n:
    if i%2==0:
        sum+=i
    i+=1
print(sum)
'''