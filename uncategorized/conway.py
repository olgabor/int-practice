#Convay`s Game of Life 
import random, time, copy 

WIDTH = 60 
HEIGHT = 20 

#Create list of lists in cells 
nextCells = []

for x in range(WIDTH): 
    column = [] # create new cell 
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0: 
            column.append('#') #add a living cell 
        else: 
            column.append(' ') #add a dead cell 
        nextCells.append(column) #nextCell is a list of column lists. 
    

while True: #Main program loop 
    print('\n\n\n\n\n\n\n') # Separte each step with newlines 
    currentCells = copy.deepcopy(nextCells)
    #print currentCells on the screen: 
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end = '') #Print the # or space 
        print() # print new line at the end of the row 
    
    #Calcualte next step`s cell based on current step`s cells: 
    for x in range(WIDTH):
        for y in range(HEIGHT):
            #Get neighborung coordinates: 
            # '% WIDTH ' ensures leftCoord is always between 0 and WIDTH -1 
            leftCoord  = (x - 1) % WIDTH 
            rightCoord = (x + 1) % WIDTH 
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            #Count number of living neighbors:
            numNeighbors = 0 
            if currentCells[leftCoord][aboveCoord] == '#': 
                numNeighbors += 1 #Top- left neighbor is alive 
            if currentCells[x][aboveCoord] == '#': 
                numNeighbors += 1 #Top neighbor is alive 
            if currentCells[rightCoord][aboveCoord] == '#':
               numNeighbors += 1 #Top-right neighbor is alive 
            if currentCells[leftCoord][y] == '#':
               numNeighbors += 1 #Left neighbor is alive 
            if currentCells[rightCoord][y] == '#':
               numNeighbors += 1 #Right neighbor is alive 
            if currentCells[leftCoord][belowCoord] == '#':
               numNeighbors += 1 #Bottom-left neighbor is alive 
            if currentCells[x][belowCoord] == '#':
               numNeighbors += 1 #Bottom neighbor is alive 
            if currentCells[rightCoord][belowCoord] == '#':
               numNeighbors += 1 #Bottom neighbor is alive 

            #set cell based on Conway`s Game Life rules: 
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3): 
                #living cells with 2 -3 neighbors stay alive: 
                nextCells[x][y] = '#' 
            elif currentCells[x][y] == ' ' and numNeighbors == 3: 
                #Dead cells with 3 neighbors become alive: 
                nextCells[x][y] = '#'
            else: 
                #everything else dies or stays dead: 
                nextCells[x][y] = ' '

    time.sleep(1)
            