n = int(input("Enter the total number of people: "))
count = 0
for i in range(n):
    age = int(input("Enter the age of the person: "))
    if 18<=age<=60:
        count+=1
print("Number of volunteers eligible to donate blood is",count)