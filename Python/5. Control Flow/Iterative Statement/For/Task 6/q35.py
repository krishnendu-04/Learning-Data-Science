n = int(input("Enter the number of customers: "))
for i in range(1,n+1):
    rating = float(input("Enter the star rating of the hotel: "))
    if rating==5:
        print("Customer ID: C00"+str(i))