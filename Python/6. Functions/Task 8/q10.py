def heat_index(temp_c, humidity):
    F = temp_c * 9/5 + 32
    HI = ( -42.379 + 2.04901523 * F 
          + 10.14333127 * humidity
          - 0.22475541* F *humidity 
          - 0.00683783 * (F**2)
          - 0.05481717 * (humidity**2)
          + 0.00122874 * (F**2) * humidity
          + 0.00085282 * F * (humidity**2)
          - 0.00000199 * (F**2) * (humidity**2))
    C = (F - 32) * 5/9
    print("Temperature:", temp_c, "°C")
    print("Humidity:", humidity, "%")
    print("Heat Index:", HI, "°F")
    print("Heat Index:", C, "°C")

    if C < 27:
        print("Comfort Level: Cool")
    elif 27 <= C <= 32:
        print("Comfort Level: Comfortable")
    elif 33 <= C <= 39:
        print("Comfort Level: Hot")
    else:
        print("Comfort Level: Danger")
    
temp = float(input("Enter the temperature in celsius: "))
hum = float(input("Enter the humidity: "))
heat_index(temp, hum)