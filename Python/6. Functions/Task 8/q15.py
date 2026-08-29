def insurance_claim(total_bill, policy_limit, coverage_pct, deductible):
    covered = min(total_bill, policy_limit) * coverage_pct / 100
    patient_amt = deductible + (total_bill - covered)
    in_amt = total_bill - patient_amt
    print("Insurance covered amount: ",covered)
    print("Amount to be paid by the patient: ",patient_amt)
    print("Insurance amount: ",in_amt)

total = float(input("Enter the total bill: "))
policy_limit = float(input("Enter the policy limit: "))
coverage = float(input("Enter the coverage percentage: "))
deductible = float(input("Enter the deductible amount: "))
insurance_claim(total, policy_limit, coverage, deductible)