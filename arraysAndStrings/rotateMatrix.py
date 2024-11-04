# DESCRIPTION: Given an image represented by a N x N matrix, where each pixel in the image is 
# represented by an integer, write a method to rotate the image by 90 degrees. Can you do this in place?

def rotateMatrixIntoNew(matrix):
    n = len(matrix)
    new_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for r in range(0, n):
        for c in range(0, n):
            new_matrix[r][c] = matrix[(n - 1) - c][r]
    
    return new_matrix

def rotateMatrixInPlace(matrix):
    n = len(matrix)

    for c in range(0, n):
        # Do a loop through just the top row
        r = 0
        for _ in range(0, n):
            # Get the current value from the number behind
            matrix[r][c] = matrix[(n - 1) - c][r]
            # Set the values to the next value in line
            next_col = (n - 1) - r
            r = c
            c = next_col

print(rotateMatrixIntoNew([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]))
print(rotateMatrixIntoNew([[3, 2, 1], [3, 2, 1], [3, 2, 1]]))
print(rotateMatrixInPlace([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]))


# [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
# [[4, 3, 2, 1], [4, 3, 2, 1], [4, 3, 2, 1], [4, 3, 2, 1]]
# 0.0 -> 3.0, 0.1 ->2.0, 0.2 -> 1.0, 0.3->0.0
# 1.0 -> 3.1, 1.1->2.1, 1.2->1.1, 1.3->0.1

# [[3, 2, 1], [3, 2, 1], [3, 2, 1]]
# [[3, 3, 3], [2, 2, 2], [1, 1, 1]]

# 0.0 -> 3.0, 3.0 -> 3.3, 3.3 -> 0.3, 0.3 -> 0.0
# low.low, high.low, high.high, low.high
# 0.1 -> 2.0, 2.0 -> 3.2, 3.2 -> 1.3, 1.3 -> 0.1
# r.c -> c + 1.r, r.c -> c + 1.r, r.c -> ?.r, r.c -> ?.r
# 1. 3 - 0 = 0, 2. 
# 0.1 -> 1.3, 1.3 -> 3.2, 3.2 -> 2.0, 2.0 -> 0.1