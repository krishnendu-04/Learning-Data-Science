lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))
for i in range(lower,upper+1):
    sum = 0
    for j in range(1,i):
        if i%j==0:
            sum+=j
    if i==sum:
        print(i,end = " ")