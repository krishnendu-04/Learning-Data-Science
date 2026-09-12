n = int(input("How many numbers to be checked? "))
num = int(input("Enter the number: "))
small = num
for i in range(1,n):
    num = int(input("Enter the number: "))
    if num<small:
        small = num
print("Smallest number is ",small)