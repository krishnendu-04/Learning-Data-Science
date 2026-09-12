total = 0
rain = int(input("Enter the amount of rainfall: "))
while(rain!=(-1)):
    total+=rain
    rain = int(input("Enter the amount of rainfall: "))
print(total)