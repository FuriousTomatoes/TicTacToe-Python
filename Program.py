from TicTacToe import *

ticTacToe = TicTacToe()

print(ticTacToe)

while(ticTacToe.Winner() == Player.Null):
    try:
        ticTacToe.Move(int(input()), int(input()))
        print(ticTacToe)
    except TicTacToeException: pass