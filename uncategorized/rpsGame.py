import random, sys 

print('Rock, Paper, Scissors')

#these variables keep track of the number of wins, lossses, and ties
wins = 0 
losses = 0 
ties = 0 

while True: # main game loop 
    print('%s Wins, %s Loses, %s Ties' % (wins, losses, ties))
    while True: 
        print('Enter your move: (r)ock, (p)aper, (s)cissors or q(uit)')
        playerMove = input()
        if playerMove == 'q': 
            sys.exit() 
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's': 
            break 
        print('type on of r, p, s  or q.') 

    #Display what the player chose: 
    if playerMove == 'r': 
        print('Rock versus...')
    elif playerMove == 'p':
        print('Paper versus...')
    elif playerMove == 's': 
        print('Scissors versus...')
        
    #Display what the computer chose: 
    randomNumber = random.randint(1, 3)
    if randomNumber == 1: 
        computerMove = 'r'
        print('Rock')
    elif randomNumber == 2:
        computerMove = 'p'
        print('Paper')
    elif randomNumber == 3: 
        computerMove = 's'
        print('Scissors')

    #Display and record th ewin/loss/ties: 
    if playerMove == computerMove: 
        print('This is a TIE')
        ties = ties + 1 
    elif playerMove == 'r' and computerMove == 's': 
        print('You WIN!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You WIN!')
        wins = wins + 1 
    elif playerMove == 's' and  computerMove == 'p':
        print('You WIN!')
        wins = wins + 1 
    elif playerMove == 'r' and computerMove == 'p': 
        print('You lose!')
        losses = losses +1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1 
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1 

