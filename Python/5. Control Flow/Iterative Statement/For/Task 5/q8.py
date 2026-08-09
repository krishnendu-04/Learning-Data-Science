num = int(input("Enter the number: "))
count = 0
for i in range(len(str(num))):
    count+=1
    num//=10
print(count)