n = int(input("Enter the number of houses: "))
for i in range(1,n+1):
    usage = float(input("Enter the usage of electricity in units: "))
    if usage<100:
        print("House number",i,"qualified for an energy saving reward")