n = int(input("Enter the number of sales: "))
for i in range(n):
    sale_amt = float(input("Enter the sale amount: "))
    if sale_amt>2000000:
        print("Luxury Sale")