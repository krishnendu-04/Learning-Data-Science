smallest = 0
n = int(input("How many numbers to be checked? "))
for i in range(n):
    num = int(input("Enter the number: "))
    if num<smallest:
        smallest = num
print("Smallest number is ",smallest)