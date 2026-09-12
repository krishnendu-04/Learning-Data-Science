num = int(input("Enter the number: "))
og = num
sum = 0
for i in range(len(str(num))):
    a = num%10
    sum+= a**len(str(og))
    num//=10
if og==sum:
    print("Armstrong Number")
else:
    print("Not an armstrong number")