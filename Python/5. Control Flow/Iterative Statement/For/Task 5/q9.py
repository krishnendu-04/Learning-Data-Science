num = int(input("Enter the number: "))
sum = 0
for i in range(len(str(num))):
    a = num%10
    sum+=a
    num//=10
print(sum)