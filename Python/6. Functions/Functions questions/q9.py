def loan_eligibility(salary):
    if salary>50000:
        print("Eligible for Loan")
    else:
        print("Not Eligible for Loan") 

sal = float(input("Enter the salary: "))
loan_eligibility(sal)