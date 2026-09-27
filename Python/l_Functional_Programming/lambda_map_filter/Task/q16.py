nums = ['10', '20','30']
filtered = list(filter(lambda num:num>15,map(lambda num:int(num),nums)))
print(filtered)