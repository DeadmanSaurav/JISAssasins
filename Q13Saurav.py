matrix1 = [[11,22,33],
          [44,55,66],
          [77,88,99]]
matrix2 = [[1,2,3],
          [4,5,6],
          [6,7,8]]
rmatrix = [[0,0,0],
          [0,0,0],
          [0,0,0]]
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        rmatrix[i][j] = matrix1[i][j] + matrix2[i][j]
for r in rmatrix:
    print(r)
