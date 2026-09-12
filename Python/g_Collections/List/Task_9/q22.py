sales = [120.50, 450.00, 75.25, 1100.99, 320.10]
print(sales)
sales.sort()
print("Top 3 sales values: ",sales[-3:])
print("Bottom 3 sales values: ",sales[:3])
print("Annual sales: ",sum(sales))