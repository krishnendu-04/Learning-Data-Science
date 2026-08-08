n = int(input("Enter the limit: "))
for n in range(2,n+1):
    flag = 0
    for i in range(2,n):
        if n%i==0:
            flag = 1
            break
    if flag>0:
        pass
    else:
        print(n,"is prime")