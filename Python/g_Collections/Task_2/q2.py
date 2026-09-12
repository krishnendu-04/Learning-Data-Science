# A list of 15 shopping cart product prices in Indian Rupees (INR)
product_prices = [
    99.00,
    1499.50,
    89.00,
    450.00,
    2499.00,
    120.00,
    750.00,
    3500.00,
    150.25,
    999.00,
    550.00,
    220.00,
    1850.00,
    65.00,
    1299.00
]
print(product_prices)
for i in product_prices:
    if i<100:
        product_prices.remove(i)
print("\n",product_prices)
