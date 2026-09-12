n = int(input("Enter the total number of days: "))
for i in range(1,n+1):
    sales = float(input("Enter the sales of the day: "))
    if sales>10000:
        print("Day",i)