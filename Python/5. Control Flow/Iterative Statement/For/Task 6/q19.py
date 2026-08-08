Base = int(input("Enter the base: "))
Exponent = int(input("Enter the exponent: "))
result = 1
for i in range(Exponent):
    result*=Base
print(result)