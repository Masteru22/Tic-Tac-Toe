from game_board import board,verify_winner,new_turn
from prints import print_tie,print_you_win

values = [[None, None, None],
          [None, None, None],
          [None, None, None]]

won=0
board(values)

while won==0:
    new_turn("X",values)

    won=verify_winner(values,"X")

    board(values)

    if won!=0:
        break
    
    new_turn("O",values)

    won=verify_winner(values,"O")
    
    board(values)


if won==1:
    print_you_win("X")
elif won==2:
    print_you_win("O")
else:
    print_tie()