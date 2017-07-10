import pygame
import time
from life import Life

# window resolution
screen_res = 1280, 720 #width, height

# initialize pygame
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode(screen_res)
clock = pygame.time.Clock()

#  setup colors
dead = 0, 0, 0
allive = 255, 255, 255

#setup board
board_size = 160, 90 #width, height
cell_size = (screen_res[0] / board_size[0], screen_res[1] / board_size[1])

# game object
life = Life(board_size)

'''
' Helper functions
'''

#define mouse handler that allows to resurect cells durring the 'animation'
def mouse_click(pos):
    x, y = pos
    life.set_board_cell(x/cell_size[0], y/cell_size[1], 1)

def draw_board(spacing=1):
    board = life.get_board()
    for y in xrange(board_size[1]):
            for x in xrange(board_size[0]):
                point = board[x][y]
                pygame.draw.rect(
                    screen,
                    allive if point == 1 else dead, [
                        x*cell_size[0],
                        y*cell_size[1],
                        cell_size[0]-spacing,
                        cell_size[1]-spacing
                    ]
                )
        
def print_intro_txt():
    print("Starting:")
    print("Board size is: {}x{}".format(board_size[0], board_size[1]))  
    print("Screen resolution is: {}x{}".format(screen_res[0], screen_res[1])) 
    print("Cell width: {}".format(cell_size[0]))
    print("Cell height: {}".format(cell_size[1]))

# finally the main loop
def  main():
    print_intro_txt()
    iterations = 0
    while True:
        # handle user input
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN: 
                mouse_click(e.pos)

            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #clear the screen
        screen.fill(dead)

        # draw the game
        draw_board()
        pygame.display.update()

        # draw iterations overlay
        pygame.display.set_caption("Iterations: {}".format(iterations))

        # calculate next game state
        life.advance()
    
        clock.tick(30)
        iterations += 1

if __name__ == "__main__":
    main()