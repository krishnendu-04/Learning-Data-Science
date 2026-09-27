nums = [i for i in range(1,31)]
div = list(filter(lambda num:num%3==0 and num%5==0,nums))
print(div)