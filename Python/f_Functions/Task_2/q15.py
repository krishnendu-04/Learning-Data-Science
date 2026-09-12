def discount(price):
    return price*0.8
price = float(input("Enter the amount: "))
dis = discount(price)
print("Discounted bill: ",dis)