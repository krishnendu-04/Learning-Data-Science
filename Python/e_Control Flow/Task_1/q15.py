n = int(input("Enter the number: "))
a = n
sum = 0
while(n>0):
    last_digit = n%10
    fact = 1
    for i in range(1,last_digit+1):
        fact*=i
    sum+=fact
    n//=10
if a==sum:
    print("Strong Number")
else:
    print("Not a strong number")