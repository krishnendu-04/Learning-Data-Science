def currency_exchange(inr_amount, rate, currency_name):
    foreign = inr_amount / rate
    charge = inr_amount * 0.015
    total_inr = inr_amount + charge
    print("Foreign Amount: ",round(foreign),currency_name)
    print("Exchange Rate: ",rate)
    print("Service Charge: ",round(charge))
    print("Total INR Paid: ",round(total_inr))

inr_amount = float(input("Enter the INR amount: "))
rate = float(input("Enter the rate of exchange: "))
currency_name = input("Enter the currency name: ")
currency_exchange(inr_amount, rate, currency_name)