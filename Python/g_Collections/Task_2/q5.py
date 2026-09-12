salaries = [15000, 52000, 60000, 75000, 18000, 90000, 62000, 25000]
print(salaries)
for i in range(len(salaries)):
    if salaries[i]<30000:
        salaries[i]+=5000
print("Updated salaries: ",salaries)