def factorial(num):
    if num==0:
        return 0
    else:
        fact = 1
        for i in range(1,num+1):
            fact*=i
        return fact

n = int(input("Enter the number: "))
factorial = factorial(n)
print(factorial)