def salary_update(salary):
    for i in range(len(salary)):
        if salary[i]<25000:
            salary[i] += salary[i]*0.1
    print("Updated salary: ")
    for i in salary:
        print(i)
    print("Average salary: ",sum(salary)/len(salary))

n = int(input("Enter the number of employees: "))
salary = []
for i in range(n):
    salary.append(float(input("Enter the salary: ")))
salary_update(salary)