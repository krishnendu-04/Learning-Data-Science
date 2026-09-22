#generate list of tuple containing 2 numbers whose sum is even
numbers = [1,2,3,4,5]
# lst = []
# for i in range(len(numbers)):
#     for j in range(len(numbers)):
#         if (numbers[i]+numbers[j])%2==0:
#             lst.append((numbers[i],numbers[j]))
# print(lst)

lst = [(i,j) for j in numbers for i in numbers if (i+j)%2==0]
print(lst)