attendance = ["Alice", "Bob", "Alice", "Charlie", "David", "Bob", "Alice"]
print(attendance)
unique = []
for i in attendance:
    if i in unique:
        pass
    else:
        unique.append(i)
print("After retrieving first occurrence: ",unique)