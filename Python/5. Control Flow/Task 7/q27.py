lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))
for i in range(lower,upper+1):
    sum = 0
    n = i
    while(n>0):
        last = n%10
        sum+=last**(len(str(i)))
        n//=10
    if i==sum:
        print(i,end = " ")