salary = []
for i in range(10):
    salary.append(float(input("Enter the salary: ")))
count = 0
print("Salaries below 25000: ")
for i in salary:
    if i>40000:
        count+=1
    if i<25000:
        print(i)
print("Count of salaries above 40000: ",count)