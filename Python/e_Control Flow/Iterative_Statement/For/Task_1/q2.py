n = int(input("How many numbers to be checked? "))
num = int(input("Enter the number: "))
large = num
for i in range(1,n):
    num = int(input("Enter the number: "))
    if num>large:
        large = num
print("Largest number is ",large)