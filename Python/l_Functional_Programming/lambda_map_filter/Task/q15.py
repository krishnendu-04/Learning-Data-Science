nums = [i for i in range(1,21)]
filtered = list(map(lambda num:num**2,filter(lambda num:num%2==0,nums)))
print(filtered)