
nums = [3,5,8,8,2,9,9,2,0,0,5]

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]
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