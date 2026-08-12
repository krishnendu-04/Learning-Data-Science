n = int(input("Enter the limit: "))
a,b = 0,1
for i in range(n):
    if a<2:
        a,b = b, a+b
    else:
        flag = 0
        for j in range(2,a):
            if a%j==0:
                flag=1
                break
        if flag==0:
            print(a, end = " ")

        a,b = b, a+b