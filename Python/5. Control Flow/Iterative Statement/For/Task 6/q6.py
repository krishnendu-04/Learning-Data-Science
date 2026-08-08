n = int(input("Enter the limit: "))
prod = 1
for i in range(1,n+1):
    if i%2==0:
        prod*=i
print("Product of all even numbers between 1 and",n,"is",prod)