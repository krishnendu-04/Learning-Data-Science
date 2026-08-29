transactions = [9000,-5000,40000,7000,-3200,-10000,-5000,65000]
deposits = 0
withdrawals = 0
for i in transactions:
    if i>0:
        deposits+=1
    else:
        withdrawals+=1
print("Number of deposits: ",deposits)
print("Number of withdrawals: ",withdrawals)
print("Total balance: ",sum(transactions))