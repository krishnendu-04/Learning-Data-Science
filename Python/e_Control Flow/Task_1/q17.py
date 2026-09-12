n = int(input("Enter the number: "))
num = n
sum = 0
while(n>0):
    digit = n%10
    sum+=digit
    n//=10
if num%sum==0:
    print("Harshad's Number")
else:
    print("Not Harshad's Number")