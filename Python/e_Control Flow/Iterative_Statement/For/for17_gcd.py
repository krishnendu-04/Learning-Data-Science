num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
print("Greatest common divisor of",num1,"and",num2,"are")
largest = 0
if num1>num2:
    small = num2
else:
    small = num1
for i in range(1,small+1):
    if num1%i==0 and num2%i==0:
        largest = i
print(largest)