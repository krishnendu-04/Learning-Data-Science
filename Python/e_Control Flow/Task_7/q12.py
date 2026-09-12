n = int(input("Enter the limit: "))
a,b = 0,1
for i in range(n):
    if a<=n:
        print(a,end = " ")
        a,b=b,a+b