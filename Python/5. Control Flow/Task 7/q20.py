n = int(input("Enter the number: "))
largest = n%10
while(n>0):
    if (n%10)>largest:
        largest = n%10
    n//=10
print("Largest digit: ",largest)