matrix = [[1,2,3],[4,5,6],[7,8,9]]
lst = [matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[i])) if i==j]
print(lst)