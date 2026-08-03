use = float(input("Enter the litres of water used: "))
if use<500:
    print("Rs.",use*2)
elif 500<=use<1000:
    print("Rs.",use*3)
else:
    print("Rs.",use*5)