temp = int(input("Enter the temperature: "))
high = temp
for i in range(6):
    temp = int(input("Enter the temperature: "))
    if temp>high:
        high = temp
print(high)