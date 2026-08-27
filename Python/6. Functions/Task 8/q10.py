def electricity_bill(units):
    if units<=50:
        return units*3.5
    elif 51<=units<=100:
        return units*4.5
    elif 101<=units<=150:
        return units*5.5
    elif 151<=units<=200:
        return units*7.5
    elif 201<=units<=250:
        return units*8.5
    else:
        return units*10

units = float(input("Enter the units consumed: "))
final = electricity_bill(units)
print("Final bill: ",final)