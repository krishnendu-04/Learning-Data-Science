lst = [{"name": "Amit", "age": 25}, {"name": "Bala","age": 17}, {"name": "Chitra", "age": 30}]
names = [i["name"] for i in lst if i["age"]>=18]
print(names)