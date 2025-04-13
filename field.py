from classes import Color, Stone, Piece, Position
import pygame

black1 = Stone(Position(0,1), Piece.Man, Color.Black)
black2 = Stone(Position(0,3), Piece.Man, Color.Black)
black3 = Stone(Position(0,5), Piece.Man, Color.Black)
black4 = Stone(Position(0,7), Piece.Man, Color.Black)

black5 = Stone(Position(1,0), Piece.Man, Color.Black)
black6 = Stone(Position(1,2), Piece.Man, Color.Black)
black7 = Stone(Position(1,4), Piece.Man, Color.Black)
black8 = Stone(Position(1,6), Piece.Man, Color.Black)

black9 = Stone(Position(2,1), Piece.Man, Color.Black)
black10 = Stone(Position(2,3), Piece.Man, Color.Black)
black11 = Stone(Position(2,5), Piece.Man, Color.Black)
black12 = Stone(Position(2,7), Piece.Man, Color.Black)



white1 = Stone(Position(5,0), Piece.Man, Color.White)
white2 = Stone(Position(5,2), Piece.Man, Color.White)
white3 = Stone(Position(5,4), Piece.Man, Color.White)
white4 = Stone(Position(5,6), Piece.Man, Color.White)

white5 = Stone(Position(6,1), Piece.Man, Color.White)
white6 = Stone(Position(6,3), Piece.Man, Color.White)
white7 = Stone(Position(6,5), Piece.Man, Color.White)
white8 = Stone(Position(6,7), Piece.Man, Color.White)

white9 = Stone(Position(7,0), Piece.Man, Color.White)
white10 = Stone(Position(7,2), Piece.Man, Color.White)
white11 = Stone(Position(7,4), Piece.Man, Color.White)
white12 = Stone(Position(7,6), Piece.Man, Color.White)


field = [
    [None, black1, None, black2, None, black3, None, black4],
    [black5, None, black6, None, black7, None, black8, None],
    [None, black9, None, black10, None, black11, None, black12],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [white1, None, white2, None, white3, None, white4, None],
    [None, white5, None, white6, None, white7, None, white8],
    [white9, None, white10, None, white11, None, white12, None]]



blacktile = pygame.image.load("img/blacktile.png")
whitetile = pygame.image.load("img/whitetile.png")

blackpiece = pygame.image.load("img/blackman.png")
whitepiece = pygame.image.load("img/whiteman.png")

blackking = pygame.image.load("img/blackking.png")
whiteking = pygame.image.load("img/whiteking.png")



"""
The following function is used to set up the field
TODO allow different field sizes
"""
def load_field(size, screen):
    screen.blit(whitetile, (0, 0))
    screen.blit(blacktile, (0, 100))
    screen.blit(whitetile, (0, 200))
    screen.blit(blacktile, (0, 300))
    screen.blit(whitetile, (0, 400))
    screen.blit(blacktile, (0, 500))
    screen.blit(whitetile, (0, 600))
    screen.blit(blacktile, (0, 700))

    screen.blit(blacktile, (100, 0))
    screen.blit(whitetile, (100, 100))
    screen.blit(blacktile, (100, 200))
    screen.blit(whitetile, (100, 300))
    screen.blit(blacktile, (100, 400))
    screen.blit(whitetile, (100, 500))
    screen.blit(blacktile, (100, 600))
    screen.blit(whitetile, (100, 700))

    screen.blit(whitetile, (200, 0))
    screen.blit(blacktile, (200, 100))
    screen.blit(whitetile, (200, 200))
    screen.blit(blacktile, (200, 300))
    screen.blit(whitetile, (200, 400))
    screen.blit(blacktile, (200, 500))
    screen.blit(whitetile, (200, 600))
    screen.blit(blacktile, (200, 700))

    screen.blit(blacktile, (300, 0))
    screen.blit(whitetile, (300, 100))
    screen.blit(blacktile, (300, 200))
    screen.blit(whitetile, (300, 300))
    screen.blit(blacktile, (300, 400))
    screen.blit(whitetile, (300, 500))
    screen.blit(blacktile, (300, 600))
    screen.blit(whitetile, (300, 700))

    screen.blit(whitetile, (400, 0))
    screen.blit(blacktile, (400, 100))
    screen.blit(whitetile, (400, 200))
    screen.blit(blacktile, (400, 300))
    screen.blit(whitetile, (400, 400))
    screen.blit(blacktile, (400, 500))
    screen.blit(whitetile, (400, 600))
    screen.blit(blacktile, (400, 700))

    screen.blit(blacktile, (500, 0))
    screen.blit(whitetile, (500, 100))
    screen.blit(blacktile, (500, 200))
    screen.blit(whitetile, (500, 300))
    screen.blit(blacktile, (500, 400))
    screen.blit(whitetile, (500, 500))
    screen.blit(blacktile, (500, 600))
    screen.blit(whitetile, (500, 700))

    screen.blit(whitetile, (600, 0))
    screen.blit(blacktile, (600, 100))
    screen.blit(whitetile, (600, 200))
    screen.blit(blacktile, (600, 300))
    screen.blit(whitetile, (600, 400))
    screen.blit(blacktile, (600, 500))
    screen.blit(whitetile, (600, 600))
    screen.blit(blacktile, (600, 700))

    screen.blit(blacktile, (700, 0))
    screen.blit(whitetile, (700, 100))
    screen.blit(blacktile, (700, 200))
    screen.blit(whitetile, (700, 300))
    screen.blit(blacktile, (700, 400))
    screen.blit(whitetile, (700, 500))
    screen.blit(blacktile, (700, 600))
    screen.blit(whitetile, (700, 700))
    load_pieces(screen)
    """
    if size == 8:
        print("12 pieces per player")
        
    
    if size == 10:
        print("20 pieces per player")
    
    if size != 10 and size != 8:
        setup_successfull = False
    """

"""
The following function loads the stones/pieces used to play the game
"""
def load_pieces(screen):
    for i in range(len(field)):
        for j in range(len(field[i])):
            obj = field[i][j]
            if obj != None:
                if obj.piece == Piece.Man and obj.color == Color.White:
                    screen.blit(whitepiece, (obj.position.y * 100 + 30, obj.position.x * 100 + 5))
                if obj.piece == Piece.King and obj.color == Color.White:
                    screen.blit(whiteking, (obj.position.y * 100 + 30, obj.position.x * 100 + 5))
                if obj.piece == Piece.Man and obj.color == Color.Black:
                    screen.blit(blackpiece, (obj.position.y * 100 + 30, obj.position.x * 100 + 5))
                if obj.piece == Piece.King and obj.color == Color.Black:
                    screen.blit(blackking, (obj.position.y * 100 + 30, obj.position.x * 100 + 5))
