orders = [
    "Burger",
    "Pizza",
    "French Fries",
    "Burger",
    "Salad",
    "French Fries",
    "Sushi",
    "Pizza",
    "Tacos",
    "French Fries"
]
print(orders)
dict1 = {}
for i in orders:
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i]+=1
print("Count of items: ",dict1)