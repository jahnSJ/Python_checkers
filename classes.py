from enum import Enum

class Color(Enum):
    White = 1
    Black = 2

class Piece(Enum):
    Man = 1
    King = 2

#position in field as index
# x is the row in the field array
# y is the column in the field array
class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Stone:
    def __init__(self, position, piece, color):
        self.position = position
        self.piece = piece
        self.color = color


class Move:
    def __init__(self, position, score, color):
        self.position = position
        self.score = score
        self.color = color#color of the stone being moved