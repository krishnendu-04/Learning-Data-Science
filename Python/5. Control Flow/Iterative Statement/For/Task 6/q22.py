n = int(input("Enter the total number of customers: "))
for i in range(n):
    bill = float(input("Enter the bill amount: "))
    if bill>3000:
        print("Gift Coupon")