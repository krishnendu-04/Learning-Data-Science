n = int(input("Enter the total number of customers: "))
for i in range(1,n+1):
    if i%5==0:
        print("Free wash")
    else: 
        print("Paid wash")