tup = ("car","bike",109.56,9000,87)
print(tup)
lst1 = list(tup)
lst1[2] = "jeep"
tup = tuple(lst1)
print(tup)