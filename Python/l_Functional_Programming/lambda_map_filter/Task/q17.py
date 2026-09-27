tup = [('Amit', 85), ('Bala', 40), ('Chitra', 92),('Deepak', 55)]
filtered = list(map(lambda i:i[0],filter(lambda j:j[1]>60,tup)))
print(filtered)