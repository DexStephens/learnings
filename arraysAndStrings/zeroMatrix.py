# DESCRIPTION: Write an algorithm such that if an element in an M x N matrix is 0, 
# its entire row and column are set to 0.

def zeroMatrix(matrix):
    rowLength = len(matrix)
    colLength = len(matrix[0])
    zeros = []

    for r in range(0, rowLength):
        for c in range(0, colLength):
            if matrix[r][c] == 0:
                zeros.append((r, c))
    
    for r, c in zeros:
        zeroRow(matrix, r, colLength)
        zeroCol(matrix, c, rowLength)

    return matrix

def zeroRow(matrix, row, colLength):
    for n in range(0, colLength):
        matrix[row][n] = 0

def zeroCol(matrix, col, rowLength):
    for n in range(0, rowLength):
        matrix[n][col] = 0

print(zeroMatrix([[1, 1, 1], [2, 0, 2], [3, 3, 3], [4, 4, 4]]))