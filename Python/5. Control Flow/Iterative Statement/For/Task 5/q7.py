n = int(input("Enter the number: "))
rev = 0
for i in range(len(str(n))):
    a = n%10
    rev = rev*10 + a
    n//=10
print("Reversed Number is",rev)