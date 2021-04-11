from enum import *

class TicTacToeException(Exception): pass
Player = IntEnum("Player", "Null X O")

a: int = 5

class TicTacToe:
    '''A simple tris engine.
    Move(int x, int y): Makes a move at (x, y). [0 - 2]
    Winner(): Returs the winner Player. [Null / X / O]'''
    def __init__(self):
        '''Inizialize'''
        self.Turn = Player.X
        self.Board = [[Player.Null] * 3 for _ in range(3)]

    def Move(self, x: int, y: int): 
        '''Move(int x, int y): Makes a move at (x, y). [0 - 2]'''
        if self.Board[x][y] != Player.Null or self.Winner() != Player.Null: raise TicTacToeException("")
        self.Board[x][y] = self.Turn
        self.Turn = Player.X if self.Turn == Player.O else Player.O

    def Winner(self) -> Player:
        '''Winner(): Returs the winner Player. [Null / X / O]'''
        for i in range(3): #Checks horizontal and vertical lines
            if(self.Board[i][i] != Player.Null):
                if(self.Board[i][0] == self.Board[i][1] == self.Board[i][2]): return self.Board[i][i]
                if(self.Board[0][i] == self.Board[1][i] == self.Board[2][i]): return self.Board[i][i]
        #Checks diagonal lines
        if(self.Board[1][1] != Player.Null and (self.Board[0][0] == self.Board[1][1] == self.Board[2][2] or self.Board[0][2] == self.Board[1][1] == self.Board[2][0])):
            return self.Board[1][1]
        return Player.Null

    def __str__(self):
        s = "+---+---+---+\n"
        for y in range(3):
            for x in range(3):
                s += f"| {' ' if self.Board[x][y] == Player.Null else self.Board[x][y].name} "
            s += "|\n+---+---+---+\n"
        return s