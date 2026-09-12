n = int(input("Enter the number of employees: "))
for i in range(1,n+1):
    packed = int(input("How many packages did you pack? "))
    if packed>200:
        print("P00"+str(i),"eligible for incentive")