def calculate_bill(price,quantity):
    return price*quantity
rate = float(input("Enter the price of the dish: "))
qty = float(input("Enter the quantity ordered: "))
total = calculate_bill(rate,qty)
print("Total bill : ",total)