price = float(input("Enter the price of the product: "))
choice = input("Do you want to add another item to the bill(yes/no): ")
total = price
while(choice!="no"):
    price = float(input("Enter the price of the product: "))
    total+=price
    choice = input("Do you want to add another item to the bill(yes/no): ")
print("Total bill: ",total)