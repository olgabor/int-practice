#Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
#Output: true 
 
board1 = [["8","3",".",".","7",".",".",".","."]
        , ["6",".",".","1","9","5",".",".","."]
        , [".","9","8",".",".",".",".","6","."]
        , ["8",".",".",".","6",".",".",".","3"]
        , ["4",".",".","8",".","3",".",".","1"]
        , ["7",".",".",".","2",".",".",".","6"]
        , [".","6",".",".",".",".","2","8","."]
        , [".",".",".","4","1","9",".",".","5"]
        , [".",".",".",".","8",".",".","7","9"]]
# Output: false

def isValidSudoku(board):

    # init data
    row, col, sub_box  = set(), set(), set()


    # validate a board
    for i in range(9):
        for j in range(9):
            if(board[i][j] != '.'):
                row_digit = (i, board[i][j])
                col_digit= (j, board[i][j])
                sub_box_digit = (i //3, j //3, board[i][j])
                # print(row_digit, col_digit, sub_box_digit)
                if ((row_digit in row )or (col_digit in col) or (sub_box_digit in sub_box)):
                    return False 

                row.add(row_digit)
                col.add(col_digit)
                sub_box.add(sub_box_digit)
            
    return True

print(isValidSudoku(board)) #True 
print(isValidSudoku(board1)) #False 