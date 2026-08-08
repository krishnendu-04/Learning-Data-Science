n = int(input("How many numbers to be chechked? "))
even=0
odd=0
for i in range(n):
    num = int(input("Enter the number: "))
    if num%2==0:
        even+=1
    else:
        odd+=1
print("Count of even numbers: ",even)
print("Count of odd numbers: ",odd)