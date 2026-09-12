n = int(input("Enter the number: "))
smallest = n%10
while(n>0):
    if n%10<smallest:
        smallest = n%10
    n//=10
print("Smallest digit: ",smallest)