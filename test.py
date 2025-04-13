import unittest
from move import *
from classes import *
from checkers import *

"""
As a reference:
https://docs.python.org/3/library/unittest.html
"""


def all_possibleMoves(field):
    for i in range(len(field)):
        for j in range(len(field[i])):
            obj2move = field[i][j]
            if obj2move != None:
                moves = possibleMoves(obj2move, field)
                print("")
                print("Moves for (" + str(i) + "," + str(j) + ")")
                if len(moves) > 0:
                    for h in range(len(moves)):
                        print("(" + str(moves[h].x) + "," + str(moves[h].y) +")")
                else:
                    print("Has no moves")

class TestStringMethods(unittest.TestCase):

    #def test_def(self):
        #self.assertEqual(,)
        #self.assertTrue()
        #self.assertFalse()

    def test_0(self):
        
        black1 = Stone(Position(0,5), Piece.Man, Color.Black)
        black2 = Stone(Position(0,7), Piece.Man, Color.Black)
        black3 = Stone(Position(1,4), Piece.Man, Color.Black)
        black4 = Stone(Position(1,6), Piece.Man, Color.Black)

        black5 = Stone(Position(2,1), Piece.Man, Color.Black)
        black6 = Stone(Position(2,3), Piece.Man, Color.Black)
        black7 = Stone(Position(2,7), Piece.Man, Color.Black)
        black8 = Stone(Position(3,0), Piece.Man, Color.Black)

        black9 = Stone(Position(3,2), Piece.Man, Color.Black)
        black10 = Stone(Position(3,6), Piece.Man, Color.Black)
        black11 = Stone(Position(7,0), Piece.King, Color.Black)
        
        white1 = Stone(Position(4,3), Piece.Man, Color.White)
        white2 = Stone(Position(4,5), Piece.Man, Color.White)
        white3 = Stone(Position(5,0), Piece.Man, Color.White)
        white4 = Stone(Position(5,2), Piece.Man, Color.White)

        white5 = Stone(Position(5,4), Piece.Man, Color.White)
        white6 = Stone(Position(6,1), Piece.Man, Color.White)
        white7 = Stone(Position(6,3), Piece.Man, Color.White)
        white8 = Stone(Position(6,7), Piece.Man, Color.White)

        white9 = Stone(Position(7,6), Piece.Man, Color.White)

        field = [
            [None, None, None, None, None, black1, None, black2],
            [None, None, None, None, black3, None, black4, None],
            [None, black5, None, black6, None, None, None, black7],
            [black8, None, black9, None, None, None, black10, None],
            [None, None, None, white1, None, white2, None, None],
            [white3, None, white4, None, white5, None, None, None],
            [None, white6, None, white7, None, None, None, white8],
            [black11, None, None, None, None, None, white9, None]]

        all_possibleMoves(field)

        self.assertFalse(check_4_win(Color.White))
        self.assertFalse(check_4_win(Color.Black))

    def test_1(self):
        black11 = Stone(Position(7,0), Piece.King, Color.Black)
        
        white1 = Stone(Position(6,1), Piece.Man, Color.White)
        
        field = [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, white1, None, None, None, None, None, None],
            [black11, None, None, None, None, None, None, None]]

        all_possibleMoves(field)

    def test_2(self):
        black11 = Stone(Position(4,3), Piece.King, Color.Black)

        field = [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, black11, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None]]

        all_possibleMoves(field)
    
    """
    def test_3(self):
        black11 = Stone(Position(4,3), Piece.King, Color.Black)
        white1 = Stone(Position(3,4), Piece.Man, Color.White)

        field = [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, white1, None, None, None],
            [None, None, None, black11, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None]]

        piecetaken(Position(4,3), Position(2,5), field)
        if field[3][4] != None:
            print("Dang 1")

        black11 = Stone(Position(4,3), Piece.King, Color.Black)
        
        white2 = Stone(Position(3,2), Piece.Man, Color.White)

        field = [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, white2, None, None, None, None, None],
            [None, None, None, black11, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None]]

        piecetaken(Position(4,3), Position(2,1), field)
        if field[3][2] != None:
            print("Dang 2")

        black11 = Stone(Position(4,3), Piece.King, Color.Black)
        
        white4 = Stone(Position(5,2), Piece.Man, Color.White)

        field = [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, black11, None, None, None, None],
            [None, None, white4, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None]]
        
        piecetaken(Position(4,3), Position(6,1), field)
        if field[5][2] != None:
            print("Dang 3")

        black11 = Stone(Position(4,3), Piece.King, Color.Black)
        
        white3 = Stone(Position(5,4), Piece.Man, Color.White)
    
        field = [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, black11, None, None, None, None],
            [None, None, None, None, white3, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None]]
        
        piecetaken(Position(4,3), Position(6,5), field)
        if field[5][4] != None:
            print("Dang 4")
    """


if __name__ == '__main__':
       unittest.main()