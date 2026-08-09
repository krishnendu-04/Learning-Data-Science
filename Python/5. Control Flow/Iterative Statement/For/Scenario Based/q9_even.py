count = 0
for i in range(10):
    num = int(input("Enter the number: "))
    if num%2==0:
        count+=1
print(count,"out of given 10 are even numbers")