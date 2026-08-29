rain = [56,78,43,90,23,34,43]
above_50 = 0
for rainfall in rain:
    if rainfall>50:
        above_50+=1
print("Rainfall above 50mm: ",above_50)
print("Average rainfall: ",sum(rain)/len(rain))