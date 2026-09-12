temp = []
for i in range(5):
    temp.append(int(input("Enter the temperature: ")))
print("Maximum temperature: ",max(temp))
print("Minimum temperature: ",min(temp))
print("Average temperature: ",sum(temp)/len(temp))