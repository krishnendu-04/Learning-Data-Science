num = int(input("Enter the number: "))
prod = 1
for i in range(len(str(num))):
    a = num%10
    prod*=a
    num//=10
print(prod)