def inventory_update():
    stock = {
        "Apple": 50,
        "Banana": 120,
        "Milk": 10
    }
    print(stock)
    item = input("Enter the item to purchase: ")
    if stock[item]>0:
        stock[item] -= 1
    else:
        print("Item out of stock")
    for i in stock:
        if stock[i]<10:
            print(i,"stock less than 10")

inventory_update()