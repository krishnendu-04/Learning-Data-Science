python = {"Amal", "Rahul", "Anjali", "Meera"}
sql = {"Sreerag", "Sneha", "Kavya", "Meera", "Hari","Anjali"}
powerbi = {"Rohan","Anjali", "Sreerag", "Parvathy", "Hari"}
print("\nEmployees with all three skills: ",python.intersection(sql.intersection(powerbi)))
print("\nEmployees with only Python: ",python-sql.union(powerbi))
print("\nEmployees with Python and SQL but not Power BI: ",python.intersection(sql)-powerbi)
print("\nEmployees having at least one skill: ",python.union(sql.union(powerbi)))
print("\nEmployees having exactly one skill: ",python-sql.union(powerbi),sql-python.union(powerbi),powerbi-python.union(sql))