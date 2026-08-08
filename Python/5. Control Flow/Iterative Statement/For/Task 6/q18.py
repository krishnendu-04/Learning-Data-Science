num1 = int(input("Enter the number: "))
num2 = int(input("Enter the number: "))
if num1>num2:
    limit = num1
else:
    limit = num2
for i in range(limit,num1*num2+1):
    if i%num1==0 and i%num2==0:
        lcm = i
        break
print(lcm)