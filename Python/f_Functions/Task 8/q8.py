import math
def quadratic_solver(a, b, c):
    D = (b**2) - (4*a*c)
    print("Discriminant: ",D)
    if D>0:
        r1 = ((-b) + math.sqrt(D)) / (2*a)
        r2 = ((-b) - math.sqrt(D)) / (2*a)
        print("Real Roots")
        print("Root 1: ",r1)
        print("Root 2: ",r2)
    elif D == 0:
        r = (-b) / (2*a)
        print("One Repeated Root: ",r)
    else:
        real = (-b) / (2*a)
        imag = math.sqrt(-D) / (2*a)

        print("Complex Roots")
        print("Root 1:", real, "+", imag, "i")
        print("Root 2:", real, "-", imag, "i")


a = float(input("Enter the quadratic coefficient: "))
b = float(input("Enter the linear coefficient: "))
c = float(input("Enter the constant term: "))
quadratic_solver(a, b, c)