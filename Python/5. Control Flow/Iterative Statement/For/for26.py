num = input("Enter the armstrong number: ")
n = int(num)
sum = 0
while(n>0):
    a = n%10
    sum += a**len(num)
    n//=10
if sum==int(num):
    print("Armstrong number")
else:
    print("Not armstrong")