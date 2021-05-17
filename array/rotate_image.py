#You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# Input: 
# Output: [[7,4,1],[8,5,2],[9,6,3]]

matrix = [[1,2,3],[4,5,6],[7,8,9]]
def rotate_image(matrix): 
    n = len(matrix[0])
    for row in range(len(matrix)): 
        for col in range(row, n): 
            matrix[row][col], matrix[col][row]  = matrix[col][row] , matrix[row][col]

    print(matrix)
    for row in range(len(matrix)):
         for col in range(n//2):
             matrix[row][col], matrix[row][-col - 1] = matrix[row][-col - 1], matrix[row][col]
             
    print(matrix)
print(rotate_image(matrix))