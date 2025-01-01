A = [[1, 2, 3],
    [4, 5, 7],
    [2, 4, 5]]

B = [[1, 2, 3],
    [4, 5, 7],
    [2, 4, 5]]

result = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] + B[i][j]


for r in result:
    print(r)
    
        

    
       
