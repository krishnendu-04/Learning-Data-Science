n = int(input("Enter the number of days: "))
for i in range(1,n+1):
    gen = float(input("Enter the electricity generated: "))
    if gen>1000:
        print("Day",i)