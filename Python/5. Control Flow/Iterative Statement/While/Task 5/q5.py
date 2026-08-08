price = float(input("Enter the price of the item: "))
total = price
while price!=0:
    price = float(input("Enter the price of the item: "))
    total+=price
print("Final bill",total)