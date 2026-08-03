use = float(input("Enter the litres of water used: "))
if use<5:
    print("Rs.100")
elif use<10:
    print("Rs.500")
elif use<=15:
    print("Rs.1000")
elif use>15:
    print("Rs.5000")