def grocery_bill():
    groceries = {
        "Rice": 60,
        "Sugar": 45,
        "Milk": 30,
        "Bread": 40,
        "Oil": 150
    }
    print(groceries)
    for i in groceries:
        groceries[i] += groceries[i]*0.05
    print("Updated grocery prices: ",groceries)
    print("Grocery above Rs.100: ")
    for i in groceries:
        if groceries[i]>100:
            print(i)

grocery_bill()