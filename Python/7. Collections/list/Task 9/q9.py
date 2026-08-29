mon_expenses = []
for i in range(5):
    mon_expenses.append(int(input("Enter monthly expenses: ")))
print("Total expense: ",sum(mon_expenses))
print("Highest expense: ",max(mon_expenses))