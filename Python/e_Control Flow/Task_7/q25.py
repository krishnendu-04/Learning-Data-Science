n1 = int(input("Enter the number: "))
n2 = int(input("Enter the number: "))
if n1>n2:
    large = n1
else:
    large = n2
for i in range(large,n1*n2+1):
    if i%n1==0 and i%n2==0:
        print(i)
        break
    