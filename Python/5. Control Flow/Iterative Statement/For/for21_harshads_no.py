num = int(input("Enter the number: "))
n = num
sum = 0
while n>0:
    a = n%10
    sum+=a
    n//=10
if num%sum==0:
    print("Harshad's Number")
else:
    print("Not Harshad's number")