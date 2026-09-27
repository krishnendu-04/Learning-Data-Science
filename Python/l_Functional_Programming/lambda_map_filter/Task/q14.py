dict1 = [{"name": "Amit", "age": 25}, {"name": "Bala","age": 17}]
adults = list(filter(lambda i:i["age"]>=18,dict1))
print(adults)