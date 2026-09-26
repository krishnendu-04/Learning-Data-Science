x =  [1, 2, 3]
y =  [4, 5, 6]
even = [(i,j) for i in x for j in y if (i+j)%2==0]
print(even)