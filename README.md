# IA for games

The goal is to create an AI to play against me. For that I implementer a min-max algorithm associated with an alpha-beta elegance to improve perfomance.


I put you a pseudo-code so that you understand what it corresponds:

![](./Readme_Content/MinMax.jpg?raw=true "Min Max Algorithm")
![](./Readme_Content/AlphaBeta.jpg?raw=true "Alpha Beta Algorithm")


## Tic Tac Toe
```cmd
python tictactoe.py
```
At first I created a tic tac toe to test the algorithm. The problem is that it's too easy to have a tie. We could not see the total potential of the application. So I decided to use a more complicated game ...

## Gomoku
```cmd
python gomoku.py
```

Gomoku is a two-player turn-based board game (Player1 with black pawns, Player2 with white pawns). <br>
The black player plays first. Each player has 60 tokens. The size of the board is 15 squares on 15 squares. The lines are numbered from 'A' to 'O' and the columns are numbered from '1' to '15'. A player may place a pawn on any free space. The first one to align 5 consecutive pawns (horizontally, vertically or diagonally) won. Otherwise, the game is declared void if there are no more counters.

 In the game of Gomoku (as for the monster), the first player has the advantage. We are interested in a variant to reduce this inequality. This is the variantelong pro:
- player1 (black) places a pawn in the center of the board (H8)
- the player2 (white) can place a piece anywhere 
- Then the player1 can place a piece anywhere except in a square of size 7 squares on 7 squares of center H8.
- Then the part is his course normally ...