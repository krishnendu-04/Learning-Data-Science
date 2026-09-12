amt = float(input("Enter the recharge amount: "))
if amt==199:
    print("1 GB/day")
elif amt==299:
    print("1.5 GB/day")
elif amt==399:
    print("2 GB/day")
else:
    print("Plan not available")