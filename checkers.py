import pygame
from pygame.locals import *
import time
import random
from move import *
from field import *
from classes import *


"""
I used the following sources:
https://www.python-lernen.de/bilder-grafiken-anzeigen-pygame.htm
https://www.pygame.org/docs/
"""

"""
it removes the taken piece
This is allowed, because the move has been checked by isLegal() in move.py
"""
def piecetaken(position_before_move : Position, position_after_move : Position):

    row = position_before_move.x
    column = position_before_move.y

    new_row = position_after_move.x
    new_column = position_after_move.y
    
    obj = field[row][column]

    #therefore make a move then check again
    #so just remove an opponent piece that is behind the pice that just moved over it
    #check if there is an opponent piece behind position after and between position before
    #for the king just check if it is on the line and if the king is infornt of the taken piece

    #I changed the signs here because I need to go backwards that means I go into the opposite Direction
    #and remove the peice there
    if obj.piece == Piece.Man:
        if obj.color == Color.White and row - new_row == 2:
            #white takes to the left \
            if column > new_column and row > new_row and obj.color == Color.White:
                field[row-1][column-1] = None

            #white takes to the right /
            if column < new_column and row > new_row and obj.color == Color.White:
                field[row-1][column+1] = None
        
        if obj.color == Color.Black and new_row - row == 2:
            #black takes to the right \
            if column < new_column and row < new_row and obj.color == Color.Black:
                field[row+1][column+1] = None

            #black takes to the left /
            if column > new_column and row < new_row and obj.color == Color.Black:
                field[row+1][column-1] = None

    else:
        # The king can take forward and backwards, so she moves just like a black and white peice
        if column < new_column and row > new_row:
            i = row
            j = column
            while i >= new_row +1 and j <= new_column-1:
                field[i][j] = None
                i-=1
                j+=1

        if column > new_column and row > new_row:
            i = row
            j = column
            while i >= new_row+1 and j >= new_column+1:
                field[i][j] = None
                i-=1
                j-=1
        
        if column < new_column and row < new_row:
            i = row
            j = column
            while i <= new_row -1 and j <= new_column-1:
                field[i][j] = None
                i+=1
                j+=1

        if column > new_column and row < new_row:
            i = row
            j = column
            while i <= new_row-1 and j >= new_column+1:
                field[i][j] = None
                i+=1
                j-=1

"""
Checks if the moved piece has reached the other side, if so then it promotes the piece to a king
"""
def promotion(position_after_move: Position):

    if field[position_after_move.x][position_after_move.y] == None:
        return

    if position_after_move.x == 0 and field[position_after_move.x][position_after_move.y].color == Color.White and field[position_after_move.x][position_after_move.y].piece == Piece.Man:
        field[position_after_move.x][position_after_move.y] = None
        king = Stone(Position(position_after_move.x,position_after_move.y), Piece.King, Color.White)
        field[position_after_move.x][position_after_move.y] = king

    if position_after_move.x == 7 and field[position_after_move.x][position_after_move.y].color == Color.Black and field[position_after_move.x][position_after_move.y].piece == Piece.Man:
        field[position_after_move.x][position_after_move.y] = None
        king = Stone(Position(position_after_move.x,position_after_move.y), Piece.King, Color.Black)
        field[position_after_move.x][position_after_move.y] = king


"""
The player who made it impossible for the opponent to move any of his pieces or who took all opponents pieces wins the game
"""
def check_4_win(color) -> bool:
    won = False
    number_of_opponent_pieces = 0
    available_moves = 0
    opponent = Color.Black if color == Color.White else Color.White
    for i in range(len(field)):
        for j in range(len(field[i])):
            obj = field[i][j]

            if obj == None:
                continue

            #check for every enemy stone if it can move
            if obj.color == opponent:
                number_of_opponent_pieces += 1
                moves = possibleMoves(obj, field)
                if len(moves) > 0:
                    available_moves += len(moves)
                """
                # it suffices to check if the piece can still move one square up as white or one square down as black
                # since the pieces can only move if that is a given. A king can move even further but only if it isnt blocked
                if obj.color == Color.White:
                    #check if the bounds are correct
                    if i-1 >= 0 and j+1 <= 7 and j-1 >= 0:
                        #check neigboring cells
                        if field[i-1][j+1] != None or field[i-1][j-1] != None:
                            #obj can move to one square
                            available_moves += 1
                        
                else:
                    #check if the bounds are correct
                    if i+1 <= 7 and j+1 <= 7 and j-1 >= 0:
                        if field[i+1][j+1] != None or field[i+1][j-1] != None:
                            #obj can move to one square
                            available_moves +=1
                """
    if number_of_opponent_pieces == 0 or available_moves == 0:
        #print("#oponnets :" + str(number_of_opponent_pieces) + " moves :" + str(available_moves))
        won = True

    return won

"""
The following function defines how the human player moves its pieces
"""
def human_move() -> bool:
    #print("Human Turn")
    moveMade = False
    position_before_move = Position(-1,-1)
    position_after_move = Position(-1,-1)
    while not moveMade:
        #fetch the wanted position
        haveMouse = False
        while not haveMouse:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                    return
                elif event.type == MOUSEBUTTONDOWN or event.type == MOUSEBUTTONUP:
                    haveMouse = True
        #find mouse
        mouse_pos = pygame.mouse.get_pos()
        row = int(mouse_pos[1] / 100)#x
        column = int(mouse_pos[0] / 100)#y
        figure = field[row][column]
        position_before_move = Position(row, column)
        pygame.event.clear()
        #find next move
        if figure != None:
            time.sleep(1)
            havenewPosition = False
            while not havenewPosition:
                for event in pygame.event.get():
                    if event.type == QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                        return
                    elif event.type == MOUSEBUTTONDOWN or event.type == MOUSEBUTTONUP:
                        havenewPosition = True
            new_mouse_pos = pygame.mouse.get_pos()
            new_row = int(new_mouse_pos[1] / 100)
            new_column = int(new_mouse_pos[0] / 100)

            #print("From ("+ str(row) + "," + str(column) +") to ("+ str(new_row) + "," + str(new_column) +")")
            
            # if the piece wasnt moved then wait for the new position
            # or if the move wasnt legal then let the player make a legal move
            if new_row == row and new_column == column:
                print("The peice you selected wasn't moved")
                continue
            elif not isLegal(position_before_move, Position(new_row, new_column), field):
                print("The move was ilegal")
                print("You tried to move from (" + str(position_before_move.x)+ "," + str(position_before_move.y) + ") to (" + str(new_row) + ","+ str(new_column)+ ")")
                continue
            piecetaken(position_before_move, Position(new_row, new_column))
            figure.position = Position(new_row, new_column)
            field[row][column] = None
            field[new_row][new_column] = figure
            position_after_move = figure.position
            moveMade = True
    #make_nextMove = take_further(position_after_move)
    promotion(position_after_move)
    win = check_4_win(Color.White)# human is always the white player

    if not win and position_before_move.x - position_after_move.x == 2:
        row = position_after_move.x
        column = position_after_move.y
        piece = field[row][column]

        if piece.piece == Piece.Man:
            pos = piece.position
                
            while pos.x == piece.position.x or pos.y == piece.position.y:
                while (row -1 > 0 and column +1 < 8 and row -2 >= 0 and column +2 < 8):
                    if field[row-1][column+1] != None:
                        if field[row-1][column+1].color == Color.Black and field[row-2][column+2] == None:
                            field[row-1][column+1] = None
                            field[row][column] = None
                            field[row-2][column+2] = piece
                            piece.position = Position(row-2,column+2)
                            promotion(piece.position)
                        else:
                            break
                    else:
                        break
                    row -= 1
                    column +=1
        
                row = piece.position.x
                column = piece.position.y
                while(row-1 > 0 and column -1 > 0 and row-2 >= 0 and column -2 >= 0):
                    if field[row-1][column-1] != None:
                        if field[row-1][column-1].color == Color.Black and field[row-2][column-2] == None:
                            field[row-1][column-1] = None
                            field[row][column] = None
                            field[row-2][column-2] = piece
                            piece.position = Position(row-2,column-2)
                            promotion(piece.position)
                        else:
                            break
                    else:
                        break
                    row -= 1
                    column -=1
                
                if pos.x != piece.position.x or pos.y != piece.position.y:
                    pos = piece.position
                else:
                    break

        else:

            pos = piece.position
                
            while pos.x == piece.position.x or pos.y == piece.position.y:

                while (row +1 < 8 and column +1 < 8 and row +2 < 8 and column +2 < 8):
                    if field[row+1][column+1] != None:
                        if field[row+1][column+1].color == Color.Black and field[row+2][column+2] == None:
                            #print("I can take further with this piece")
                            field[row+1][column+1] = None
                            field[row][column] = None
                            field[row+2][column+2] = piece
                            piece.position = Position(row+2,column+2)
                        else:
                            break
                    else:
                        break
                    row += 1
                    column +=1
        
                while(row+1 < 8 and column -1 > 0 and row+2 < 8 and column -2 >= 0):
                    if field[row+1][column-1] != None:
                        if field[row+1][column-1].color == Color.Black and field[row+2][column-2] == None:
                            #print("I can take further with this piece")
                            field[row+1][column-1] = None
                            field[row][column] = None
                            field[row+2][column-2] = piece
                            piece.position = Position(row+2,column-2)
                        else:
                            break
                    else:
                        break
                    row += 1
                    column -=1
            
                while (row -1 > 0 and column +1 < 8 and row -2 >= 0 and column +2 < 8):
                    if field[row-1][column+1] != None:
                        if field[row-1][column+1].color == Color.Black and field[row-2][column+2] == None:
                            field[row-1][column+1] = None
                            field[row][column] = None
                            field[row-2][column+2] = piece
                            piece.position = Position(row-2,column+2)
                        else:
                            break
                    else:
                        break
                    row += 1
                    column +=1
        
                row = piece.position.x
                column = piece.position.y
                while(row-1 > 0 and column -1 > 0 and row-2 >= 0 and column -2 >= 0):
                    if field[row-1][column-1] != None:
                        if field[row-1][column-1].color == Color.Black and field[row-2][column-2] == None:
                            field[row-1][column-1] = None
                            field[row][column] = None
                            field[row-2][column-2] = piece
                            piece.position = Position(row-2,column-2)
                        else:
                            break
                    else:
                        break
                    row += 1
                    column -=1
                    
                if pos.x != piece.position.x or pos.y != piece.position.y:
                    pos = piece.position
                else:
                    break
        #print("Final position: (" + str(piece.position.x) + "," +  str(piece.position.y) +")")
    return moveMade

def computer(depth: int):
    #print("Computer Turn")
    
    my_move = alpha_beta(Color.Black, depth)

    piece = field[my_move[0].position.x][my_move[0].position.y]

    #print("Computer moved from (" + str(my_move[0].position.x) + "," + str(my_move[0].position.y) + ") to (" + str(my_move[1].position.x) + "," + str(my_move[1].position.y) + ")")

    piecetaken(my_move[0].position, my_move[1].position)

    field[my_move[0].position.x][my_move[0].position.y] = None
    field[my_move[1].position.x][my_move[1].position.y] = piece
    piece.position = my_move[1].position
   
    promotion(my_move[1].position)
    win = check_4_win(Color.Black)

    if not win and my_move[1].position.x - my_move[0].position.x == 2:
        #if two rows are between them then a piece was taken as the move was legal
        row = my_move[1].position.x
        column = my_move[1].position.y

        if piece.piece == Piece.Man:
            while (row +1 < 8 and column +1 < 8 and row +2 < 8 and column +2 < 8):
                if field[row+1][column+1] != None:
                    if field[row+1][column+1].color == Color.White and field[row+2][column+2] == None:
                        #print("I can take further with this piece")
                        field[row+1][column+1] = None
                        field[row][column] = None
                        field[row+2][column+2] = piece
                        piece.position = Position(row+2,column+2)
                        promotion(piece.position)
                    else:
                        break
                else:
                    break
                row += 1
                column +=1
        
            while(row+1 < 8 and column -1 > 0 and row+2 < 8 and column -2 >= 0):
                if field[row+1][column-1] != None:
                    if field[row+1][column-1].color == Color.White and field[row+2][column-2] == None:
                        #print("I can take further with this piece")
                        field[row+1][column-1] = None
                        field[row][column] = None
                        field[row+2][column-2] = piece
                        piece.position = Position(row+2,column-2)
                        promotion(piece.position)
                    else:
                        break
                else:
                    break
                row += 1
                column -=1
        else:
            while (row -1 > 0 and column +1 < 8 and row -2 >= 0 and column +2 < 8):
                if field[row-1][column+1] != None:
                    if field[row-1][column+1].color == Color.White and field[row-2][column+2] == None:
                        field[row-1][column+1] = None
                        field[row][column] = None
                        field[row-2][column+2] = piece
                        piece.position = Position(row-2,column+2)
                    else:
                        break
                else:
                    break
                row += 1
                column +=1
        
            row = piece.position.x
            column = piece.position.y
            while(row-1 > 0 and column -1 > 0 and row-2 >= 0 and column -2 >= 0):
                if field[row-1][column-1] != None:
                    if field[row-1][column-1].color == Color.White and field[row-2][column-2] == None:
                        field[row-1][column-1] = None
                        field[row][column] = None
                        field[row-2][column-2] = piece
                        piece.position = Position(row-2,column-2)
                    else:
                        break
                else:
                    break
                row += 1
                column -=1
            
            while (row +1 < 8 and column +1 < 8 and row +2 < 8 and column +2 < 8):
                if field[row+1][column+1] != None:
                    if field[row+1][column+1].color == Color.White and field[row+2][column+2] == None:
                        #print("I can take further with this piece")
                        field[row+1][column+1] = None
                        field[row][column] = None
                        field[row+2][column+2] = piece
                        piece.position = Position(row+2,column+2)
                    else:
                        break
                else:
                    break
                row += 1
                column +=1
        
            while(row+1 < 8 and column -1 > 0 and row+2 < 8 and column -2 >= 0):
                if field[row+1][column-1] != None:
                    if field[row+1][column-1].color == Color.White and field[row+2][column-2] == None:
                        #print("I can take further with this piece")
                        field[row+1][column-1] = None
                        field[row][column] = None
                        field[row+2][column-2] = piece
                        piece.position = Position(row+2,column-2)
                    else:
                        break
                else:
                    break
                row += 1
                column -=1
     #   print("Final position: (" + str(piece.position.x) + "," +  str(piece.position.y) +")")

"""
The following function is based on alpha beta prunning.
For further information see https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
"""
def alpha_beta(color, searchdepth = 5, alpha=-10000000, beta=10000000):
    if searchdepth == 0:
        return [Move(Position(-1,-1),0, color), Move(Position(-1,-1),0, color)]
    
    piece2move = Move(Position(-1,-1), alpha, Color.Black) 
    bestMove = Move(Position(-1,-1), alpha, Color.Black)
    score_of_move = 0

    if color == Color.Black:

        for i in range(len(field)):
            for j in range(len(field[i])):
                obj2move = field[i][j]
                if obj2move != None:
                    if obj2move.color == Color.Black:
                        moves = possibleMoves(obj2move, field)
                        if len(moves) > 0:

                            # make a move
                            field[i][j] = None
                            idx = random.randint(0,len(moves)-1) if len(moves) > 1 else 0
                            field[moves[idx].x][moves[idx].y] = obj2move
                            obj2move.position = Position(moves[idx].x, moves[idx].y)

                            # check score of move
                            if check_4_win(Color.Black):
                                score_of_move = 10
                            elif moves[idx].x - i == 2:
                                score_of_move = 10
                            elif moves[idx].x == 7 and obj2move.piece == Piece.Man: 
                                score_of_move = 4
                            else:
                                score_of_move = 2
                        
                            nextMove = alpha_beta(Color.White, searchdepth-1, -beta, -bestMove.score)

                            if score_of_move > bestMove.score:
                                bestMove = Move(obj2move.position, score_of_move, Color.Black)
                                piece2move = Move(Position(i,j), score_of_move, Color.Black)

                            #take move back
                            field[i][j] = obj2move
                            field[moves[idx].x][moves[idx].y] = None
                            obj2move.position = Position(i,j)

                            if nextMove[1].score > bestMove.score:
                                if nextMove[1].score >= beta:
                                    return nextMove
    else:
        for i in range(len(field)):
            for j in range(len(field[i])):
                obj2move = field[i][j]
                if obj2move != None:
                    if obj2move.color == Color.White:
                        moves = possibleMoves(obj2move, field)
                        if len(moves) > 0:

                            #make a move
                            field[i][j] = None
                            idx = random.randint(0,len(moves)-1) if len(moves) > 1 else 0
                            field[moves[idx].x][moves[idx].y] = obj2move
                            obj2move.position = Position(moves[idx].x, moves[idx].y)

                            #check score of move
                            if check_4_win(Color.White):
                                score_of_move = 10
                            elif i - moves[idx].x == 2:
                                score_of_move = 10
                            elif moves[idx].x == 0 and obj2move.piece == Piece.Man: 
                                score_of_move = 4
                            else: 
                                score_of_move = 1

                            nextMove = alpha_beta(Color.Black, searchdepth-1, -beta, -bestMove.score)
                        
                            if score_of_move > bestMove.score:
                                bestMove = Move(obj2move.position, score_of_move, Color.White)
                                piece2move = Move(Position(i,j), score_of_move, Color.White)

                            field[i][j] = obj2move
                            field[moves[idx].x][moves[idx].y] =  None
                            obj2move.position = Position(i,j)

                            if nextMove[1].score > bestMove.score:
                                if nextMove[1].score > beta:
                                    return nextMove
    return [piece2move, bestMove]