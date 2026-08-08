n = int(input("Enter the number: "))
og = n
rev = 0
for i in range(len(str(n))):
    a = n%10
    rev = rev*10 + a
    n//=10
if og==rev:
    print("Palindrome Number")
else:
    print("Not Palindrome")