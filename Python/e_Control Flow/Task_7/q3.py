n = int(input("Enter the number: "))
num = n
rev = 0
while(n>0):
    a = n%10
    rev = rev*10+a
    n//=10
if rev==num:
    print("Palindrome")
else:
    print("Not palindrome")