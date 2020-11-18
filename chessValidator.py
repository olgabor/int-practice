#write a function that return True / False wheather the board is valid or not 
#Board is valid if: 
    # has exactly one black king and exactly one white king 
    # each player can only have at most 16 pieces, most 8 pawns 
    # all pieces must be on a valid space from '1a' to '8h' (cant be on a space '9z')
    # piece names bedin with either a 'w', 'b' 
    # to represent white or black, folowed by 'pawn', 'knight', 'bishop', 'rook', 'queen' or 'king'

board = {'1a': 'bking','2a': 'bqueen','3a': 'brook','4a': 'brook',
'5a': 'bknight','6a': 'bknight','7a':'bbishop','8a': 'bbishop',
'1b': 'bpawn','2b': 'bpawn','3b': 'bpawn','4b':'bpawn',
'5b': 'bpawn','6b': 'bpawn','7b': 'bpawn','8b': 'bpawn',
'1c': 'wking','2c': 'wqueen','3c': 'wrook','4c': 'wrook',
'5c': 'wbishop','6c': 'wbishop','7c': 'wknight','8c':'wknight',
'1e': 'wpawn','2e': 'wpawn','3e': 'wpawn','4e': 'wpawn',
'5e': 'wpawn','6e': 'wpawn','7e': 'wpawn','8e': 'wpawn',
'1f': '','2f': '','3f': '','4f': '','5f': '','6f': '','7f': '','8f': '',
'1g': '','2g': '','3g': '','4g': '','5g': '','6g': '','7g': '','8g': '',
'1h': '','2h': '','3h': '','4h': '','5h': '','6h': '','7h': '','8h': ''}

def isValidChessBoard(board):
    bpiece = 0
    wpiece = 0
    check = []
    totalCount = {}
    
    #counts frequency of eack key in board dict 
    for value in board.values():
        totalCount.setdefault(value, 0)
        totalCount[value] =  totalCount[value] + 1

    #creates the list of valid pieces
    for i in range(1,9):
        for letter in ['a', 'b', 'c', 'e', 'f', 'h', 'g']:
            check.append(str(i) + str(letter))

    #has exactly one black king and exactly one white king 
    if totalCount['bking'] > 1 or totalCount['wking'] > 1: 
        print('The board is not valid! There is more than one king, bking count is' , totalCount['bking'], ',', 'wking count is', totalCount['wking'])
        return False
    
    #each player can only have at most 16 pieces, most 8 pawns 
    for k in board.values():
        try:
           if k[0] == 'w':
                wpiece = wpiece + 1 
           if k[0] == 'b':
                bpiece = bpiece + 1

           #piece names bedin with either a 'w', 'b' 
           elif k[0] != 'w' and k[0] != 'b':
               print('The board is not valid! Value', k, 'doesnt start with b or w')
               return False
            
        except IndexError:
            pass

    if wpiece > 16 or totalCount['wpawn'] > 8: 
        print('The board is not valid! White pieces count is more than 16 pieces', wpiece)
        return False 
    if bpiece > 16 or totalCount['bpawn'] > 8: 
        print('The board is not valid! Black pieces count is more than 16 pieces', bpiece)
        return False 
    
    #all pieces must be on a valid space from '1a' to '8h' (cant be on a space '9z')
    for key in board.keys(): 
        if key not in check: 
            print('The board is not valid! The key: ' + key \
                + ' doesn`t belong here')
            return False 

    #checks if all expected keys are present in board 
    for item in check: 
        if item not in board.keys():
            print('The board is not valid! The key: ' + item \
                + ' is missing')
            return False 

    return True 

print(isValidChessBoard(board))

