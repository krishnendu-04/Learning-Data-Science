import math

def projectile(velocity, angle_deg):
    radians = math.radians(angle_deg)
    g = 9.8
    max_height = ((velocity**2)*(math.sin(radians) ** 2))/(2*g)
    time = (2*velocity*math.sin(radians))/g
    Range = ((velocity**2)*math.sin(2*radians))/g

    print("Maximum Height: ",max_height,"m")
    print("Time of Flight: ",time,"s")
    print("Horizontal Range: ",Range,"m")

angle = float(input("Enter the angle in degrees: "))
velocity = float(input("Enter the velocity of the ball in m/s: "))
projectile(velocity, angle)