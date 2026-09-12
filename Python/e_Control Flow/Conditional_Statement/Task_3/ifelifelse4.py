num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2:"))
op = input("Enter the operator to perform calculation: ")
if op=='+':
    print("Sum of",num1,"and",num2,"is",num1+num2)
elif op=='-':
    print("Difference of",num1,"and",num2,"is",num1-num2)
elif op=='*':
    print("Product of",num1,"and",num2,"is",num1*num2)
elif op=='/':
    print("Quotient of",num1,"and",num2,"is",num1/num2)
else:
    print("Invalid operation")