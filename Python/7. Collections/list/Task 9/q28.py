nums = [10,20,30,20,40,10,50,30]
unique = []
for num in nums:
    if num not in unique:
        unique.append(num)
print("Unique list: ",unique)