import pygame 

from setup.draw_board import draw_board
from setup.put_pieces import put_pieces

SCREEN_HEIGHT = 720 
SCREEN_WIDTH = 720 


position = [
        ["Rb", "Nb", "Bb", "Qb", "Kb", "Bb", "Nb", "Rb"],
        ["Pb", "Pb", "Pb", "Pb", "Pb", "Pb", "Pb", "Pb"],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["Pw", "Pw", "Pw", "Pw", "Pw", "Pw", "Pw", "Pw"],
        ["Rw", "Nw", "Bw", "Qw", "Qw", "Bw", "Nw", "Rw"],
        ]


def render_screen():
    pygame.init() 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    while running:
        
        draw_board(screen, clock, SCREEN_HEIGHT, SCREEN_WIDTH)
        put_pieces(screen, position)
        for event in pygame.event.get():
            if event == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(60)
    

def main():
    render_screen()


main()


