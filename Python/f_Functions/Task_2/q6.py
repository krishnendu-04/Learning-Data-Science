def salary(basic_salary):
    return basic_salary*1.1
sal = float(input("Enter your basic salary: "))
final = salary(sal)
print("Final salary: ",final)