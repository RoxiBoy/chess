import pygame 

from setup.draw_board import draw_board
from setup.put_pieces import put_pieces

from game.move import select_rect
from game.move import move

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
        ["Rw", "Nw", "Bw", "Qw", "Kw", "Bw", "Nw", "Rw"],
        ]


def render_screen():
    pygame.init() 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    click_locked = False

    draw_board(screen, clock, SCREEN_HEIGHT, SCREEN_WIDTH)
    put_pieces(screen, position)

    select_or_target = True # True for select and False for target

    selected_square = []
    target_sqaure = []
    selected_rect = ""
    selected_piece = ""
    target_rect = ""
    target_piece = ""

    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and click_locked == False:
                click_locked == True
                mouse_pos = pygame.mouse.get_pos()
            
                clicked_rect, piece, clicked_square = select_rect(screen, mouse_pos, position)

                if select_or_target == True:
                    if piece == '':
                        continue 
                    else:
                        selected_rect = clicked_rect
                        selected_piece = piece
                        selected_square = clicked_square
                        select_or_target = False
                        draw_board(screen, clock, SCREEN_HEIGHT, SCREEN_WIDTH)
                        pygame.draw.rect(screen, (255, 0, 0), selected_rect) 
                        put_pieces(screen, position)
                else:
                    # TODO Check valid move
                    if piece == "":
                        target_rect = clicked_rect
                        target_piece = ""
                        target_sqaure = clicked_square
                        select_or_target = True

                        new_position = move(screen, selected_square, selected_piece, target_sqaure, target_piece, position)
                    else:
                        target_rect = clicked_rect
                        target_piece = piece
                        target_sqaure = clicked_square

                        select_or_target = True

                    
                    target_piece = ""
                    target_sqaure = ""
                    target_rect = ""


                if select_or_target:
                    print("Select Now") 
                else: 
                    print("Target Now")


            if event.type == pygame.MOUSEBUTTONUP:
                click_locked = False


        for event in pygame.event.get():
            if event == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(7)
    

def main():
    render_screen()


main()


