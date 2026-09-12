def employee_salary():
    employees = {
        101: 25000,
        102: 75000,
        103: 35000,
        104: 80000
    }
    print(employees)
    for i in employees:
        employees[i] +=3000
    print("After updated salaries: ",employees)
    print("Employees earning above 50000: ")
    for j in employees:
        if employees[j]>50000:
            print(j)

employee_salary()