purchase_amount = float(input("Enter the purchase amount: "))
if purchase_amount<2000:
    print("No Discount")
elif 2000<=purchase_amount<=4999:
    print("5% Discount")
elif 5000<=purchase_amount<=10000:
    print("10% Discount")
elif purchase_amount>10000:
    print("20% Discount")
else:
    print("Invalid amount")