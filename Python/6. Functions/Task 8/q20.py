def loan_emi(principal, annual_rate, years):
    r = annual_rate / (12*100)
    n = years*12
    EMI = (principal * r * (1 + r)**n) / ((1 + r)**n- 1)
    balance = principal
    total_interest = 0
    print("Month\t\tEMI\t\t\tInterest\t\tPrincipal\t\tBalance")
    for i in range(1,n+1):
        interest = balance * r
        principal_part = EMI - interest
        balance = balance - principal_part
        total_interest+=interest
        if i<=6:
            print("\n",i,"\t\t",round(EMI,2),"\t\t\t",round(interest,2),"\t\t\t",round(principal_part,2),"\t\t\t",round(balance,2))
    print("\nTotal Interest: ",round(total_interest))

p = float(input("Enter the principal amount: "))
t = int(input("Enter the time taken in years: "))
rate = float(input("Enter the rate of interest: "))
loan_emi(p,rate,t) 