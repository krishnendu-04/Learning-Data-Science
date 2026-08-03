num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
num3 = float(input("Enter number 3: "))
if num1>num2 and num1>num3:
    print(num1,"is the greatest")
elif num2>num1 and num2>num3:
    print(num2,"is the greatest")
elif num1==num2 and num1>=num3:
    print(num1,"is the greatest")
elif num2==num3 and num2>=num1:
    print(num2,"is the greatest")
elif num1==num3 and num1>=num2:
    print(num1,"is the greatest")
else:
    print(num3,"is the greatest")