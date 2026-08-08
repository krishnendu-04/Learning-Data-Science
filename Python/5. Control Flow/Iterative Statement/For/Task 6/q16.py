num = int(input("Enter the number: "))
count = 0
print("Number of factors of",num,"are")
for i in range(1,num+1):
    if num%i==0:
        count+=1
print(count)