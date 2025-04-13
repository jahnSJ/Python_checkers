from classes import *

"""
Determines all possible moves for the given piece
"""
def possibleMoves(piece: Stone, field) -> list[Move]:
    moves = []
    row = piece.position.x
    column = piece.position.y

    if piece.piece == Piece.Man:

        if piece.color == Color.White:
            #check right diagonal
            if row -1 >= 0 and column+1 < 8:
                if field[row-1][column+1] == None:
                    moves.append(Position(row-1,column+1))
            
            if row -1 >= 0 and column+1 < 8 and row-2 >= 0 and column+2 < 8:
                if field[row-1][column+1] != None:
                    if field[row-1][column+1].color == Color.Black and field[row-2][column+2] == None:
                        moves.append(Position(row-2,column+2))
            
            #ckeck left diagonal
            if row -1 >= 0 and column-1 >= 0:
                if field[row-1][column-1] == None:
                    moves.append(Position(row-1,column-1))

            if row -1 >= 0 and column-1 > 0 and row-2 >= 0 and column-2 > 0:
                if field[row-1][column-1] != None:
                    if field[row-1][column-1].color == Color.Black and field[row-2][column-2] == None:
                        moves.append(Position(row-2,column-2))
        else:
            #black takes to the right 
            if row +1 < 8 and column +1 < 8:
                if field[row+1][column+1] == None:
                    moves.append(Position(row+1,column+1))
            
            if row +1 < 8 and column +1 < 8 and row +2 < 8 and column +2 < 8:
                if field[row+1][column+1] != None:
                    if field[row+1][column+1].color == Color.White and field[row+2][column+2] == None:
                        moves.append(Position(row+2,column+2))
            
            #black takes to the left /
            if row+1 < 8 and column -1 >= 0:
                if field[row+1][column-1] == None:
                    moves.append(Position(row+1, column-1))
            
            if row+1 < 8 and column -1 > 0 and row+2 < 8 and column -2 >= 0:
                if field[row+1][column-1] != None:
                    if field[row+1][column-1].color == Color.White and field[row+2][column-2] == None:
                        moves.append(Position(row+2, column-2))
    else:
        # if piece is a King then check the following:

        temp_row = row-1
        temp_column = column+1
        while temp_row >= 0 and temp_column < 8:
            if field[temp_row][temp_column] == None:
                moves.append(Position(temp_row,temp_column))
            else:
                if field[temp_row][temp_column].color == piece.color:
                    break
                else:
                    if temp_row-1 >= 0 and temp_column+1 < 8:
                        if field[temp_row-1][temp_column+1] == None:
                            moves.append(Position(temp_row-1,temp_column+1))
                            break
            temp_row -=1
            temp_column +=1
            
        
        temp_row = row-1
        temp_column = column-1
        while temp_row >= 0 and temp_column >= 0:
            if field[temp_row][temp_column] == None:
                moves.append(Position(temp_row,temp_column))
            else:
                if field[temp_row][temp_column].color == piece.color:
                    break
                else:
                    if temp_row-1 >= 0 and temp_column-1 > 0:
                        if field[temp_row-1][temp_column-1] == None:
                            moves.append(Position(temp_row-1,temp_column-1))
                            break
            temp_row -= 1
            temp_column -= 1

        temp_row = row+1
        temp_column = column+1
        while temp_row < 8 and temp_column < 8:
            if field[temp_row][temp_column] == None:
                moves.append(Position(temp_row,temp_column))
            else:
                if field[temp_row][temp_column].color == piece.color:
                    break
                else:
                    if temp_row+1 < 8 and temp_column+1 < 8:
                        if field[temp_row+1][temp_column+1] == None:
                            moves.append(Position(temp_row+1,temp_column+1))
                            break
            temp_row += 1
            temp_column += 1

        temp_row = row+1
        temp_column = column-1
        while temp_row < 8 and temp_column >= 0:
            if field[temp_row][temp_column] == None:
                moves.append(Position(temp_row,temp_column))
            else:
                if field[temp_row][temp_column].color == piece.color:
                    break
                else:
                    if temp_row+1 < 8 and temp_column-1 > 0:
                        if field[temp_row+1][temp_column-1] == None:
                            moves.append(Position(temp_row+1,temp_column-1))
                            break
            temp_row += 1
            temp_column -= 1
    return moves


all_legal_squares = [Position(0,1), Position(0,3), Position(0,5), Position(0,7),
                     Position(1,0), Position(1,2), Position(1,4), Position(1,6),
                     Position(2,1), Position(2,3), Position(2,5), Position(2,7),
                     Position(3,0), Position(3,2), Position(3,4), Position(3,6),
                     Position(4,1), Position(4,3), Position(4,5), Position(4,7),
                     Position(5,0), Position(5,2), Position(5,4), Position(5,6),
                     Position(6,1), Position(6,3), Position(6,5), Position(6,7),
                     Position(7,0), Position(7,2), Position(7,4), Position(7,6),
                     ]

"""
Checks if the move made is within the boundries of the field
"""
def move2legal_square(position_after_move):
    legal = False
    for i in all_legal_squares:
        if position_after_move.x == i.x and position_after_move.y == i.y:
            legal = True

    return legal


"""
The following function checks if the move was legal.
To do so it assumes that the position before move was already legal.
Check the choosen position before setting the piece to the choosen position (position_after_move)

A move consists of either taking a peice or moving forward as a piece

position_before_move is the position at which the piece is now
position_after_move is the position after the move has been made
"""
def isLegal(position_before_move, position_after_move, field):
    legal = True
    row = position_before_move.x
    column = position_before_move.y
    obj = field[row][column]

    #print("BEFORE: ("+ str(row) + "," + str(column) +")")

    new_row = position_after_move.x
    new_column = position_after_move.y

    #print("AFTER: ("+ str(new_row) + "," + str(new_column) +")")

    # it is not possible to move nothing and you cant land on a occupied square
    #if obj == None or field[new_row][new_column] != None:
    if obj == None:
        print("Ilegal 0")
        return False

    #if an illegal square was selected then it was an illegal move
    #if it was illegal then there is no reason to check the move further
    if not move2legal_square(position_after_move):
        print("Ilegal 1")
        return False

    #each man can only move one stp up or two steps when they take a piece
    # if they can take multiple pieces then the turn is extended by giving the player another turn.
    # So it suffices to check if the turn made was legal
    #white pieces can only move up the board
    if obj.piece == Piece.Man and obj.color == Color.White:
           # if the square to which the piece goes is empty then it must be next to the square the pieces started from
           # however if the square to move to isnt empty then it must have taken an opposing piece
           # otherwise it was an illegal move

           # I check every diagonal, because each peice can only go into one of these directions
           # so all squares along the diagonal are the set of all possible moves

           #check right diagonal
        if row > new_row and column < new_column and obj.color == Color.White:
            i = row
            j = column
            #either go one step up or two steps to jump over an enemy
            if row -1 == new_row and column +1 == new_column:
                return True
            elif field[i-1][j+1] != None:
                if row == new_row +2  and column +2 == new_column and field[i-1][j+1].color == Color.Black:
                    return True
                else:
                    return False
            else:
                print("Ilegal 2")
                return False
            
            #ckeck left diagonal
        elif row > new_row and column > new_column and obj.color == Color.White:
            i= row
            j = column
            if row -1 == new_row and column -1 == new_column:
                return True
            elif  field[i-1][j-1] != None:
                if row == new_row +2  and column  == new_column +2 and field[i-1][j-1].color == Color.Black:
                    return True
                else:
                    return False
            else:
                print("Ilegal 3")
                return False
                
        else:
            print("Ilegal 4")
            #any other case must be illegal as there are no other possibilitys for a white man to move
            legal = False

    #black pieces can only move down the board
    elif obj.piece == Piece.Man and obj.color == Color.Black:

        #black takes to the right \
        if row < new_row and column < new_column and obj.color == Color.Black:
            i = row
            j = column
            if row +1 == new_row and column +1 == new_column:
                return True
            elif field[i+1][j+1] != None:
                if row +2 == new_row  and column +2 == new_column and field[i+1][j+1].color == Color.White:
                    return True
                else:
                    return False

            else:
                print("Ilegal 5")
                return False

        #black takes to the left /
        elif row < new_row and column > new_column and obj.color == Color.Black:
            i = row
            j = column
            if row +1 == new_row and column -1 == new_column:
                return True
            elif field[i+1][j-1] != None:
                if row +2 == new_row and column -2 == new_column and field[i+1][j-1].color == Color.White:
                    return True
                else:
                    return False
            else:
                print("Ilegal 6")
                return False
        else:
            print("Ilegal 7")
            legal = False
    
    #the king has more than one square to move to, so just check if it is at a diagonal
    else:

        #to top right
        if row > new_row and column < new_column:

            i = row-1
            j = column+1
            enemy_pieces = 0
            canTake = False
            enemy_position = Position(-1,-1)

            while i > new_row +1 and j < new_column-1:
                if i < 0 or j > 7:
                    print("Ilegal 8")
                    print("At (" + str(i) + "," + str(j) + ")")
                    legal = False
                    break

                if field[i][j] != None:

                    if field[i][j].color != obj.color:
                        enemy_pieces += 1
                        canTake = True
                        enemy_position = Position(i,j)

                    if field[i][j].color == obj.color:
                        print("Ilegal 9")
                        print("At (" + str(i) + "," + str(j) + ")")
                        #it is not allowed to jump over pieces from the same color
                        legal = False
                        break
                i-=1
                j+=1

            # if an enemy piece was encountered then the moved piece has to be right behind the taken enemy
            # so its wrong if it isnt right behind it
            # or if there was more then one enemy being jumped over
            if enemy_pieces > 1:
                print("Ilegal 10")
                legal = False

            if canTake:
                if not (enemy_position.x == new_row +1 and enemy_position.y == new_column-1):
                    #check the position before the destination of the mved piece
                    print("Ilegal 11")
                    print("At (" + str(enemy_position.x) + "," + str(enemy_position.y) + ")")
                    legal = False

        #to top left
        if row > new_row and column > new_column:

            i = row-1
            j = column-1
            enemy_pieces = 0
            canTake = False
            enemy_position = Position(-1,-1)

            while i > new_row+1 and j > new_column+1:
                if i < 0 or 0 > j:
                    print("Ilegal 12")
                    print("At (" + str(i) + "," + str(j) + ")")
                    legal = False
                    break

                if field[i][j] != None:
                    if field[i][j].color != obj.color:
                        enemy_pieces += 1
                        canTake = True
                        enemy_position = Position(i,j)

                    if field[i][j].color == obj.color:
                        print("Ilegal 13")
                        print("At (" + str(i) + "," + str(j) + ")")
                        #it is not allowed to jump over pieces from the same color
                        legal = False
                        break
                i-=1
                j-=1

            if enemy_pieces > 1:
                print("Ilegal 14")
                legal = False

            if canTake:
                if not (enemy_position.x == new_row +1 and enemy_position.y == new_column+1):
                    print("Ilegal 15")
                    print("At (" + str(enemy_position.x) + "," + str(enemy_position.y) + ")")
                    legal = False
        
        #to bottom right
        if row < new_row and column < new_column:

            i = row+1
            j = column+1
            enemy_pieces = 0
            canTake = False
            enemy_position = Position(-1,-1)

            while i < new_row -1 and j < new_column-1:
                if i > 7 or j > 7:
                    print("Ilegal 16")
                    print("At (" + str(i) + "," + str(j) + ")")
                    legal = False
                    break

                if field[i][j] != None:
                    if field[i][j].color != obj.color:
                        enemy_pieces += 1
                        canTake = True
                        enemy_position = Position(i,j)

                    if field[i][j].color == obj.color:
                        print("Ilegal 17")
                        print("At (" + str(i) + "," + str(j) + ")")
                        #it is not allowed to jump over pieces from the same color
                        legal = False
                        break
                i+=1
                j+=1

            if enemy_pieces > 1:
                print("Ilegal 18")
                legal = False
                
            if canTake:
                if not (enemy_position.x == new_row -1 and enemy_position.y == new_column-1):
                    print("Ilegal 19")
                    print("At (" + str(enemy_position.x) + "," + str(enemy_position.y) + ")")
                    legal = False

        #to bottom left
        if row < new_row and column > new_column:
            i = row+1
            j = column-1
            enemy_pieces = 0
            canTake = False
            enemy_position = Position(-1,-1)

            while i < new_row-1 and j > new_column+1:
                if i > 7 or j < 0:
                    print("Ilegal 20")
                    print("At (" + str(i) + "," + str(j) + ")")
                    legal = False
                    break
                
                if field[i][j] != None:
                    if field[i][j].color != obj.color:
                        enemy_pieces += 1
                        canTake = True
                        enemy_position = Position(i,j)

                    if field[i][j].color == obj.color:
                        print("Ilegal 21")
                        print("At (" + str(i) + "," + str(j) + ")")
                        #it is not allowed to jump over pieces from the same color
                        legal = False
                        break
                i+=1
                j-=1

            if enemy_pieces > 1:
                print("Ilegal 22")
                legal = False
                
            if canTake:
                if not (enemy_position.x == new_row -1 and enemy_position.y == new_column+1):
                    print("Ilegal 23")
                    print("At (" + str(enemy_position.x) + "," + str(enemy_position.y) + ")")
                    legal = False

    return legal
