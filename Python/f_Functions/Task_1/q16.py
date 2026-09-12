def sales_commission(salesperson_name, monthly_sales):
    if monthly_sales < 50000:
        com = 3/100
    elif 50000 <= monthly_sales <= 100000:
        com = 5/100
    elif 100000 < monthly_sales <= 200000:
        com = 8/100
    elif monthly_sales > 200000:
        com = 12/100
    bonus = 0
    if monthly_sales>150000:
        bonus = 5000
    total = com * monthly_sales + bonus
    print("Salesperson: ",salesperson_name)
    print("Monthly Sales: ",monthly_sales)
    print("Commission: ",com * monthly_sales)
    print("Bonus: ",bonus)
    print("Total earnings: ",total)

name = input("Enter your name: ")
sales = float(input("Enter your monthly sales: "))
sales_commission(name, sales)