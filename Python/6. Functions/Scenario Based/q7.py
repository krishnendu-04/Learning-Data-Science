def ohms_law(V=None, I=None, R=None):
    if V is not None and I is not None:
        R = V/I
    elif I is not None and R is not None:
        V = I*R
    elif V is not None and R is not None:
        I = V/R
    else:
        print("No enough parameters are available! ")
        return None
    P = V*I
    print("Resistance: ",R)
    print("Power: ",P)

V = input("Enter Voltage (or press Enter): ")
I = input("Enter Current (or press Enter): ")
R = input("Enter Resistance (or press Enter): ")

if V:
    V = float(V)
else:
    V = None
if I:
    I = float(I)
else: 
    I = None
if R:
    R = float(R)
else:
    R = None

ohms_law(V, I, R)