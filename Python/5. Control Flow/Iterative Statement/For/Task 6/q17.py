num1 = int(input("Enter the number: "))
num2 = int(input("Enter the number: "))
if num1>num2:
    limit = num2
else:
    limit = num1
for i in range(1,limit+1):
    if num1%i==0 and num2%i==0:
        hcf = i
print(hcf)