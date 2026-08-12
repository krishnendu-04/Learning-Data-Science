lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))
for i in range(lower,upper+1):
    rev = 0
    n = i
    while(n>0):
        last = n%10
        rev= rev*10 + last
        n//=10
    if i==rev:
        print(i,end = " ")