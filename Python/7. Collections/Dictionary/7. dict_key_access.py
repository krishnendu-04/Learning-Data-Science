dict1 = {"car":3000,"bike":2000,"bus":7500,"lorry":10000,"jeep":7500}

#Methods
print(dict1.keys())
print(dict1.values())

print(dict1.get("bike"))
print(dict1.get("car"))

dict1.update({"cycle":1000})
dict1.update({"motorcycle":500,"boat":8000})
print(dict1)

dict1.pop("lorry")
print(dict1)

dict1.popitem()
print(dict1)

dict2 = dict1.copy()
print(dict2)

dict1["Auto"] = 3500
print(dict1)

dict1["cycle"] = 800
print(dict1)

del dict1["motorcycle"]
print(dict1)