emp = ("EMP101", "EMP102", "EMP103","EMP104","EMP105","EMP106")
print(emp)
id = input("Enter the employee ID to search for: ")
if id in emp:
    print("Employee ID exists")
else:
    print("Employee ID does not exist")