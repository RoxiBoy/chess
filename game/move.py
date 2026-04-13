import pygame

def select_rect(surface, mouse_pos, position):
    X_sqaure = int(mouse_pos[0]/90)
    Y_sqaure = int(mouse_pos[1]/90)

    piece = position[Y_sqaure][X_sqaure]

    selected_square = [Y_sqaure, X_sqaure]
    selected_rect = pygame.Rect(X_sqaure*90, Y_sqaure*90, 90, 90)

    return selected_rect, piece, selected_square

def move(surface, selected_square, selected_piece, target_square, target_piece, position):
    
    Y_selected = selected_square[0]
    X_selected = selected_square[1]

    Y_target = target_square[0]
    X_target = target_square[1]

    print("Selected Piece: ", selected_piece)
    print("Target Piece: ", target_piece)

    print("Selected Square: ", selected_square)
    print("Target Square: ", target_square)

    position[Y_target][X_target] = selected_piece
    position[Y_selected][X_selected] = ""

    print(position)

    return position
