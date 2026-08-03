lower = 1
upper = 100
even_sum = 0
odd_sum = 0
while lower<=upper:
    if lower%2==0:
        even_sum+=lower
    else:
        odd_sum+=lower
    lower+=1
print("Odd sum is",odd_sum)
print("Even sum is",even_sum)