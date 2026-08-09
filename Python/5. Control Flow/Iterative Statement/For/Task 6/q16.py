n = int(input("Enter the total number of donors: "))
for i in range(n):
    contribution = float(input("Enter the contribution: "))
    if contribution>=1000:
        print("Thank You")