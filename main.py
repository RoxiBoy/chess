import pygame 

from setup.draw_board import draw_board
from setup.put_pieces import put_pieces

from game.move import select_rect
from game.move import move
from game.move import validate_turn

from services.validate_move import is_move_valid 

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
black_pieces = ["Rb", "Nb", "Bb", "Qb", "Kb", "Pb"]
white_pieces = ["Rw", "Nw", "Bw", "Qw", "Kw", "Pw"]


def render_screen():
    pygame.init() 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    click_locked = False

    def render_board_pieces(screen, clock, SCREEN_HEIGHT, SCREEN_WIDTH, selected_rect = ""):
        draw_board(screen, clock, SCREEN_HEIGHT, SCREEN_WIDTH)
        if selected_rect != "":
            pygame.draw.rect(screen, (255, 0, 0), selected_rect) 
        put_pieces(screen, position)

    render_board_pieces(screen, clock, SCREEN_HEIGHT, SCREEN_WIDTH)

    current_turn = True #True for White's turn and False for Black's turn 
    select_or_target = True # True for select and False for target

    selected_square = []
    target_sqaure = []
    selected_rect = ""
    selected_piece = ""
    target_rect = ""
    target_piece = ""
    selected_piece_moves = []

    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and click_locked == False:
                click_locked == True
                mouse_pos = pygame.mouse.get_pos()
            
                clicked_rect, clicked_piece, clicked_square = select_rect(screen, mouse_pos, position)

                if select_or_target == True: # Select
                    is_selection_valid = validate_turn(clicked_piece, current_turn)
                    if is_selection_valid == False:
                        continue
                    else:
                        selected_rect = clicked_rect
                        selected_piece = clicked_piece
                        selected_square = clicked_square
                        select_or_target = False
                        # get_all_moves(selected_square, selected_piece, position, selected_piece_moves)
                        render_board_pieces(screen, clock, SCREEN_HEIGHT, SCREEN_WIDTH, selected_rect = selected_rect) 
                else: # Target
                    # TODO Check valid move
                    target_rect = clicked_rect
                    target_piece = ""
                    target_square = clicked_square
                    select_or_target = True

                    is_move_valid = is_move_valid(selected_piece, selected_square, position, target_square)
                    if is_move_valid == True:

                        next_turn = move(screen, selected_square, selected_piece, target_square, target_piece, current_turn, position)
                        render_board_pieces(screen, clock, SCREEN_HEIGHT, SCREEN_WIDTH, selected_rect = selected_rect)
                        if next_turn == False:
                            current_turn = False 
                        else:
                            current_turn = True 
                    else:
                        selected_square = []
                        target_sqaure = []
                        selected_rect = ""
                        selected_piece = ""
                        target_rect = ""
                        target_piece = ""
                        render_board_pieces(screen, clock, SCREEN_HEIGHT, SCREEN_WIDTH)

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


