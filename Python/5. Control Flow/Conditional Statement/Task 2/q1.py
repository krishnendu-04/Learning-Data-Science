purchase_amount = int(input("Enter the purchase amount: "))
discount_amount = purchase_amount*(10/100)
if (purchase_amount>=5000):
    print("Customer receives a discount of",discount_amount)
    print("Final amount: ",purchase_amount-discount_amount)
else:
    print("Customer does not receive a discount")
    print("Final amount: ",purchase_amount)