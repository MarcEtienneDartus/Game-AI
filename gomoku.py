import time
from random import randint

def Max(grid,depth,a,b,possibleMove,root):
    if(depth == 0 or CheckVictory(grid)!=0):
        return eval(grid)

    max = -1000000
    x = 0
    y = 0

    for index in range(len(possibleMove)):
        line = possibleMove[index][0]
        column = possibleMove[index][1]
        if(grid[line][column] == 0):
            grid[line][column] = 2
            tmp = Min(grid,depth-1,a,b,possibleMove)
            # print(line,column,tmp)
            if(tmp > max or (tmp == max and randint(0, 1)%2==0)):
                max = tmp
                x = line
                y = column
                if(max>=b):
                    grid[line][column] = 0
                    return max
                if(max>a):
                    a = max
            grid[line][column] = 0
    if(root):
        grid[x][y] = 2
        SearchMove(x,y,grid,possibleMove)
    else:
        return max
    
def Min(grid,depth,a,b,possibleMove):
    if(depth == 0 or CheckVictory(grid)!=0):
        return eval(grid)

    min = 1000000

    for index in range(len(possibleMove)):
        line = possibleMove[index][0]
        column = possibleMove[index][1]
        if(grid[line][column] == 0):
            grid[line][column] = 1
            tmp = Max(grid,depth-1,a,b,possibleMove,False)
            if(tmp < min or (tmp == min and randint(0, 1)%2==0)):                
                min = tmp
                if(min<=a):
                    grid[line][column] = 0
                    return min
                if(min<b):
                    b = min
            grid[line][column] = 0
    return min
    
def eval(grid):
    nbCellFilled = 0
    for ligne in range(15):
        for colonne in range(15):
            if(grid[ligne][colonne] != 0):
                nbCellFilled += 1
    
    vainqueur = CheckVictory(grid)
    if( vainqueur == 2 ):
        return 100000 - nbCellFilled
    elif( vainqueur == 1 ):
        return -100000 + nbCellFilled
    return EvaluateVictory(grid,2) - EvaluateVictory(grid,1)

def EvaluateVictory(grid,symbolValue):
    nbPoint = 0

    #Check Points sur les lignes
    ligne = 0
    while(ligne<15):
        colonne = 0
        while(colonne<15):
            possibleForWinning = True
            index = 0
            symbolCount = 0
            while(possibleForWinning and index<5 and colonne+index<15):
                if(grid[ligne][colonne+index] != 0 and grid[ligne][colonne+index] != symbolValue):
                    possibleForWinning = False
                if(grid[ligne][colonne+index] == symbolValue):
                    symbolCount += 1
                if(grid[ligne][colonne+index]==0 or grid[ligne][colonne+index]==symbolValue):
                    index += 1
            if(possibleForWinning and index==5 and symbolCount>1):
                nbPoint += 10**(symbolCount-1)
            colonne +=1
        ligne += 1
   
    #Check Points sur les colonnes
    colonne = 0
    while(colonne<15):
        ligne = 0
        while(ligne<15):
            possibleForWinning = True
            index = 0
            symbolCount = 0
            while(possibleForWinning and index<5 and ligne+index<15):
                if(grid[ligne+index][colonne]!=0 and grid[ligne+index][colonne]!=symbolValue):
                    possibleForWinning = False
                if(grid[ligne+index][colonne]==symbolValue):
                    symbolCount += 1
                if(grid[ligne+index][colonne]==0 or grid[ligne+index][colonne]==symbolValue):
                    index+=1
            if(possibleForWinning and index==5 and symbolCount>1):
                nbPoint += 10**(symbolCount-1)
            ligne +=1
        colonne += 1

    #Check Points sur les diagonales droites
    ligne = 0
    while(ligne<15):
        colonne = 0
        while(colonne<15):
            possibleForWinning = True
            index = 0
            symbolCount = 0
            while(possibleForWinning and index<5 and ligne+index<15 and colonne+index<15):
                if(grid[ligne+index][colonne+index]!=0 and grid[ligne+index][colonne+index]!=symbolValue):
                    possibleForWinning = False
                if(grid[ligne+index][colonne+index]==symbolValue):
                    symbolCount += 1
                if(grid[ligne+index][colonne+index]==0 or grid[ligne+index][colonne+index]==symbolValue):
                    index += 1
            if(possibleForWinning and index==5 and symbolCount>1):
                nbPoint += 10**(symbolCount-1)
            colonne +=1
        ligne += 1

    #Check Points sur les diagonales gauches
    ligne = 0
    while(ligne<15):
        colonne = 14
        while(colonne>=0):
            possibleForWinning = True
            index = 0
            symbolCount = 0
            while(possibleForWinning and index<5 and ligne+index<15 and colonne-index>=0):
                if(grid[ligne+index][colonne-index]!=0 and grid[ligne+index][colonne-index]!=symbolValue):
                    possibleForWinning = False
                if(grid[ligne+index][colonne-index]==symbolValue):
                    symbolCount += 1
                if(grid[ligne+index][colonne-index]==0 or grid[ligne+index][colonne-index]==symbolValue):
                    index += 1
            if(possibleForWinning and index==5 and symbolCount>1):
                nbPoint += 10**(symbolCount-1)
            colonne -=1
        ligne += 1
    return nbPoint

def CheckVictory(grid):
    victory = 0

    #Check Victoire sur les lignes
    ligne = 0
    isSearching = True
    while(victory==0 and isSearching and ligne<15):
        colonne = 0
        while(victory==0 and isSearching and colonne<15):
            isVictory = True
            index = 0
            while(isVictory and index<4 and colonne+index<14):
                if(grid[ligne][colonne+index]==0):
                    isVictory = False
                else:
                    if(grid[ligne][colonne+index]==grid[ligne][colonne+index+1]):
                        index += 1
                    else:
                        isVictory = False
            if(isVictory and index==4):
                victory = grid[ligne][colonne]
                isSearching = False
            colonne +=1
        ligne += 1
    
    
    #Check Victoire sur les colonnes
    colonne = 0
    isSearching = True
    while(victory==0 and isSearching and colonne<15):
        ligne = 0
        while(victory==0 and isSearching and ligne<15):
            isVictory = True
            index = 0
            while(isVictory and index<4 and ligne+index<14):
                if(grid[ligne+index][colonne]==0):
                    isVictory = False
                else:
                    if(grid[ligne+index][colonne]==grid[ligne+index+1][colonne]):
                        index += 1
                    else:
                        isVictory = False
            if(isVictory and index==4):
                victory = grid[ligne][colonne]
                isSearching = False
            ligne +=1
        colonne += 1

    #Check Victoire sur les diagonales droites
    ligne = 0
    isSearching = True
    while(victory==0 and isSearching and ligne<15):
        colonne = 0
        while(victory==0 and isSearching and colonne<15):
            isVictory = True
            index = 0
            while(isVictory and index<4 and ligne+index<14 and colonne+index<14):
                if(grid[ligne+index][colonne+index]==0):
                    isVictory = False
                else:
                    if(grid[ligne+index][colonne+index]==grid[ligne+index+1][colonne+index+1]):
                        index += 1
                    else:
                        isVictory = False
            if(isVictory and index==4):
                victory = grid[ligne][colonne]
                isSearching = False
            colonne +=1
        ligne += 1

    #Check Victoire sur les diagonales gauches
    ligne = 0
    isSearching = True
    while(victory==0 and isSearching and ligne<15):
        colonne = 14
        while(victory==0 and isSearching and colonne>=0):
            isVictory = True
            index = 0
            while(isVictory and index<4 and ligne+index<14 and colonne-index>0):
                if(grid[ligne+index][colonne-index]==0):
                    isVictory = False
                else:
                    if(grid[ligne+index][colonne-index]==grid[ligne+index+1][colonne-index-1]):
                        index += 1
                    else:
                        isVictory = False
            if(isVictory and index==4):
                victory = grid[ligne][colonne]
                isSearching = False
            colonne -=1
        ligne += 1

    return victory

def DisplayGrid(grid):
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O']
    for colonne in range(15):
        if(colonne==0):
            print('   '+alphabet[colonne],end=' ')
        else:
            print(alphabet[colonne],end=' ')
    print()
    for ligne in range(15):
        for colonne in range(15):
            symbol = '.'
            if(grid[ligne][colonne]==1):
                symbol = 'o'
            if(grid[ligne][colonne]==2):
                symbol = 'x'
            if(colonne == 0):
                if(ligne<9):
                    print(' '+str(ligne+1),end=' ')
                else:
                    print(ligne+1,end=' ')
            print(symbol,end=' ')
        print()

def SearchMove(x,y,grid,possibleMove):
    if([x,y] in possibleMove):
        possibleMove.remove([x,y])
    for ligne in range(x-1,x+2):
        for colonne in range(y-1,y+2):
            if(ligne>=0 and colonne>=0 and ligne<15 and colonne<15 and grid[ligne][colonne]==0):
                if(not([ligne,colonne] in possibleMove)):
                    possibleMove.append([ligne,colonne])
                

def game():
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O']
    grid = [[0 for line in range(15)] for line in range(15)]
    nbPlay = 0
    startChoice = input('Do you want to begin ?(Y/N):')
    possibleMove=[]
    humanPlaying = False
    if(startChoice=='Y' or startChoice=='y'):
        humanPlaying = True
    while(CheckVictory(grid)==0 and nbPlay<120):
        DisplayGrid(grid)
        if(nbPlay==0):
            if(humanPlaying):
                grid[7][7] = 1
            else:
                grid[7][7] = 2
            SearchMove(7,7,grid,possibleMove)
            humanPlaying = not(humanPlaying)
        else:
            if(humanPlaying):
                WaitingForPlacement = True
                while WaitingForPlacement:
                    print('You are "o"')
                    line = 0
                    column = 0
                    if(nbPlay == 1):
                        line = int(input('On wich line do you want to play ? (1-4 et 12-15):'))-1
                        column = alphabet.index(input('On wich column do you want to play ? (A-D et L-O):').upper())
                    else:
                        line = int(input('On wich line do you want to play ? (1-15):'))-1
                        column = alphabet.index(input('On wich column do you want to play ? (A-O):').upper())
                    if(grid[line][column] != 0 or line<0 or line>15 or column<0 or column>15 or (nbPlay == 1 and ((line>3 and line<11) or (column>3 and column<11) ))):
                        print('Impossible move')
                    else:
                        grid[line][column] = 1
                        SearchMove(line,column,grid,possibleMove)
                        WaitingForPlacement = False
                humanPlaying = False
            else:
                if(nbPlay==1):
                    ligne = randint(3, 11)
                    colonne = randint(3, 11)
                    haut = randint(0, 1)
                    if(ligne!=3 and ligne != 11):
                        y = ligne
                        if(haut==1):
                            x = 3
                        else:
                            x = 11
                    else:
                        x = colonne
                        y = ligne
                    grid[y][x] = 2
                    SearchMove(y,x,grid,possibleMove)
                else:
                    Max(grid,2,-10000000,10000000,possibleMove,True)
                humanPlaying = True
        nbPlay += 1

        
    DisplayGrid(grid)

    victory = CheckVictory(grid)
    if(victory==1):
        print('You win!')
    if(victory==2):
        print('You Loose !')
    if(victory!=1 and victory!=2):
        print('Draw !')



if __name__ == '__main__':
    game()