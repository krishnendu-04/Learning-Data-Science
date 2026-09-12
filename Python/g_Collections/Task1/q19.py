def bank_accounts():
    accounts = {
        "ACC101": 1500.50,
        "ACC102": 250.00,
        "ACC103": 5420.75
    }
    print(accounts)
    acc_no = input("Enter the account number to deposit money: ")
    if acc_no in accounts:
        deposit = float(input("Enter the amount to deposit: "))
        accounts[acc_no] += deposit
    else:
        print("Account not found")
    max_bal = 0
    for i in accounts:
        if accounts[i]>max_bal:
            max_acc = i
            max_bal = accounts[i]
    print("Account with highest bank balance: ",max_acc)
    for k,v in accounts.items():
        print(f"{k}:{v}")



bank_accounts()