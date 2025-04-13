import pygame
from field import *
from checkers import *
from classes import *
from test import all_possibleMoves

#on Windows use: py -m pip install -U pygame --user
#  run with: py ./main.py

#on Ubuntu use: sudo apt install python3-pygame
# run with: python3 ./main.py

if __name__ == '__main__':

    #print("10x10 or 8x8 Field?")
    input = 8 # TODO change to user input from window

    pygame.init()
    W, H = 800, 800
    screen = pygame.display.set_mode((W, H))
    clock = pygame.time.Clock()
    
    run_game = True

    #pygame.draw.circle(screen, "red", (0,1), 40)
   # pygame.draw.rect(screen, "brown",(0,1), 40)
   #pygame.draw.rect(screen, "white",(0,1), 40)
    #pygame.draw.circle(screen, "red", (0,1), 40)

    # Main Game loop
    while run_game:
        for event in pygame.event.get():
            # End the game if [ESC] or [X] was pressed
            if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                run_game = False
                break
        
        screen.fill("brown")
        load_field(input, screen)
        pygame.display.flip()

        screen.fill("brown")
        if not human_move():
            break
        pygame.display.flip()

        if check_4_win(Color.White):
            print("You won the game")
            #all_possibleMoves(field)
            run_game = False
            break

        screen.fill("brown")
        load_field(input, screen)
        pygame.display.flip()

        screen.fill("brown")
        computer(5)
        pygame.display.flip()

        if check_4_win(Color.Black):
            print("The computer won the game")
            #all_possibleMoves(field)
            run_game = False
            break

        #set framerate
        clock.tick(60)
    
    pygame.quit()
