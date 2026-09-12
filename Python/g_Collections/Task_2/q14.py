daily = [30000,-2500,6500,25000,-10000,-5000,-800,4200,50000]
print(daily)
deposits = []
withdrawals = []
for transactions in daily:
    if transactions>0:
        deposits.append(transactions)
    else:
        withdrawals.append(transactions)
print("Deposits: ",deposits)
print("Withdrawals: ",withdrawals)