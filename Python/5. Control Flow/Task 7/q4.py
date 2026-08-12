n = int(input("Enter the number: "))
temp = n
sum = 0
while(n>0):
    a = n%10
    sum += a**3
    n//=10
if temp==sum:
    print("Armstrong")
else:
    print("Not armstrong")