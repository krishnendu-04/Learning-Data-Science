def check_temperature(temp):
    if temp>25:
        print("Hot Temperature")
    elif 15<=temp<=25:
        print("Normal Temperature")
    elif temp<15:
        print("Cold Temperature")
temp = float(input("Enter the temperature recorded in celsius: "))
check_temperature(temp)