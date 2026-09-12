def rental_analysis(property_value, monthly_rent, monthly_expenses):
    gross_income = monthly_rent * 12
    total_expenses = monthly_expenses * 12
    net_income = gross_income - total_expenses
    tax = 0 
    if net_income>250000:
        tax = net_income*0.3
        net_income-=tax
    roi = (net_income / property_value) * 100
    print("Gross Annual Income: ",gross_income)
    print("Total Expenses: ",total_expenses)
    print("Tax: ",tax)
    print("Net Income: ",net_income)
    print("ROI: ",str(round(roi))+"%")

    
value = float(input("Enter the value of the property: "))
rent = float(input("Enter the monthly rent: "))
expenses = float(input("Enter the monthly expenses: "))
rental_analysis(value, rent, expenses)