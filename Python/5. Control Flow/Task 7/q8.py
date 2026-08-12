n = int(input("Enter the number: "))
prod = 1
while(n>0):
    digit = n%10
    prod*=digit
    n//=10
print("Product of digits: ",prod)