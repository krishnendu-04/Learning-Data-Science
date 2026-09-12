n = int(input("Enter the number of orders: "))
for i in range(1,n+1):
    delivery_time = int(input("Enter the delivery time in mins: "))
    if delivery_time>60:
        print("O00"+str(i))