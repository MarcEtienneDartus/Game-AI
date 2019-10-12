def Max(grid,depth,a,b,root):
    if(depth == 0 or CheckVictory(grid)!=0):
        return eval(grid)

    max = -10000
    x = 0
    y = 0

    for line in range(3):
        for column in range(3):
            if(grid[line][column] == 0):
                grid[line][column] = 2
                tmp = Min(grid,depth-1,a,b)
                if(tmp > max):
                    max = tmp
                    x = line
                    y = column
                    if(max>=b):
                        return max
                    if(a>max):
                        a = max
                grid[line][column] = 0
    if(root):
        grid[x][y] = 2
    else:
        return max
    

def Min(grid,depth,a,b):
    if(depth == 0 or CheckVictory(grid)!=0):
        return eval(grid)

    min = 10000

    for line in range(3):
        for column in range(3):
            if(grid[line][column] == 0):
                grid[line][column] = 1
                tmp = Max(grid,depth-1,a,b,False)
                if(tmp < min):                
                    min = tmp
                    if(min<=a):
                        return min
                    if(b<min):
                        b = min
                grid[line][column] = 0
    return min
    

def eval(grid):
    nbCellFilled = 0
    for ligne in range(3):
        for colonne in range(3):
            if(grid[ligne][colonne] != 0):
                nbCellFilled += 1
    
    vainqueur = CheckVictory(grid)
    if( vainqueur == 2 ):
        return 1000 - nbCellFilled
    elif( vainqueur == 1 ):
        return -1000 + nbCellFilled
    return EvaluateVictory(grid,1) - EvaluateVictory(grid,2)

def EvaluateVictory(grid,symbolValue):
    nbPoint = 0
    for x in range(3):
        possibleForWinning = True
        y = 0
        symbolCount = 0
        while possibleForWinning and y<3:
            if(grid[x][y] != 0 and grid[x][y] != symbolValue):
                possibleForWinning = False
            if(grid[x][y] == symbolValue):
                symbolCount +=1
            y+=1
            if(y==3 and symbolCount>1 and possibleForWinning):
                nbPoint += 1
        
        possibleForWinning = True
        y = 0
        symbolCount = 0
        while possibleForWinning and y<3:
            if(grid[y][x] != 0 and grid[y][x] != symbolValue):
                possibleForWinning = False
            if(grid[y][x] == symbolValue):
                symbolCount +=1
            y+=1
            if(y==3 and symbolCount>1 and possibleForWinning):
                nbPoint += 1

    possibleForWinning = True
    y = 0
    symbolCount = 0
    while possibleForWinning and y<3:
        if(grid[y][y] != 0 and grid[y][y] != symbolValue):
            possibleForWinning = False
        if(grid[y][y] == symbolValue):
            symbolCount +=1
        y+=1
        if(y==3 and symbolCount>1 and possibleForWinning):
            nbPoint += 1
    
    possibleForWinning = True
    y = 0
    symbolCount = 0
    while possibleForWinning and y<3:
        if(grid[2-y][y] != 0 and grid[2-y][y] != symbolValue):
            possibleForWinning = False
        if(grid[2-y][y] == symbolValue):
            symbolCount +=1
        y+=1
        if(y==3 and symbolCount>1 and possibleForWinning):
            nbPoint += 1
    
    return nbPoint

def CheckVictory(grid):
    victory = 0
    for index in range(3):
        if(grid[index][0] == grid[index][1] and grid[index][1] == grid[index][2] and grid[index][0] != 0):
            victory = 1
            if(grid[index][0] == 2):
                victory = 2
        if(grid[0][index] == grid[1][index] and grid[1][index] == grid[2][index] and grid[0][index] != 0):
            victory = 1
            if(grid[0][index] == 2):
                victory = 2
    if(grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2] and grid[0][0] != 0):
        victory = 1
        if(grid[0][0] == 2):
            victory = 2
    if(grid[2][0] == grid[1][1] and grid[1][1] == grid[0][2] and grid[2][0] != 0):
        victory = 1
        if(grid[2][0] == 2):
            victory = 2
    return victory


def DisplayGrid(grid):
    for ligne in range(3):
        for colonne in range(3):
            symbol = '.'
            if(grid[ligne][colonne]==1):
                symbol = 'o'
            if(grid[ligne][colonne]==2):
                symbol = 'x'
            print(symbol,end=' ')
        print()

def game():
    grid = [[0 for line in range(3)] for line in range(3)]
    nbPlay = 0        
    startChoice = input('Do youwant to begin ?(Y/N):')
    humanPlaying = False
    if(startChoice=='Y' or startChoice=='y'):
        humanPlaying = True
    while(CheckVictory(grid)==0 and nbPlay<9):
        DisplayGrid(grid)
        if(humanPlaying):
            WaitingForPlacement = True
            while WaitingForPlacement:
                placementChoice = int(input('You are "o", Where do you want to play ? (1-9):'))
                line = int((placementChoice-1)/3)
                column = int((placementChoice-1)%3)
                if(grid[line][column] != 0):
                    print('Impossible move')
                else:
                    grid[line][column] = 1
                    WaitingForPlacement = False
            humanPlaying = False
        else:
            humanPlaying = True
            print()
            Max(grid,9-nbPlay,-100000,100000,True)
        nbPlay += 1

        
    DisplayGrid(grid)

    victory = CheckVictory(grid)
    if(victory==1):
        print('You win !')
    if(victory==2):
        print('You Loose !')
    if(victory!=1 and victory!=2 ):
        print('Draw !')


if __name__ == '__main__':
    game()
