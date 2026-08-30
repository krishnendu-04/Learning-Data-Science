stock_quantities = [15, 42, 0, 8, 114, 27, 5]
print(stock_quantities)
print("Stock quantities with less than 10: ")
for i in range(len(stock_quantities)):
    if stock_quantities[i]<10:
        print("Product",i+1)
stock_quantities.remove(0)
print("Updated stock quantities: ",stock_quantities)
print("Total stock: ",sum(stock_quantities))