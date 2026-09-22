dict1 = {"car":3200,"bike":2000,"bus":6000,"lorry":7000,"jeep":5000,"bicycle":1000}
lst1 = [k for k,v in dict1.items() if v>3000]
print(lst1)