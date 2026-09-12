n1 = int(input("Enter the number: "))
n2 = int(input("Enter the number: "))
if n1>n2:
    small = n2
else:
    small = n1
for i in range(1,small+1):
    if n1%i==0 and n2%i==0:
        greatest = i
print("Greatest common divisors: ",greatest)