salary = float(input("Enter your salary: "))
if salary<20000:
    print("Not Eligible for Bank Loan")
elif 20000<=salary<=39999:
    print("Eligible for Rs.2 Lakhs Bank Loan")
elif 40000<=salary<=79999:
    print("Eligible for Rs.5 Lakhs Bank Loan")
elif 80000<=salary:
    print("Eligible for Rs.10 Lakhs Bank Loan")