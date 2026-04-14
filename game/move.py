import pygame

def select_rect(surface, mouse_pos, position):
    X_sqaure = int(mouse_pos[0]/90)
    Y_sqaure = int(mouse_pos[1]/90)

    piece = position[Y_sqaure][X_sqaure]

    selected_square = [Y_sqaure, X_sqaure]
    selected_rect = pygame.Rect(X_sqaure*90, Y_sqaure*90, 90, 90)

    return selected_rect, piece, selected_square


def detect_piece_color(piece):
    color_code = piece[1]
    if color_code == 'b':
        return False 
    else:
        return True 


def detect_valid_selection(piece, current_turn):
    if piece == "":
        return False

    print("Piece: ", piece)
    piece_color = detect_piece_color(piece)

    if piece_color == current_turn:
        return True
    else:
        return False
    

def move(surface, selected_square, selected_piece, target_square, target_piece, current_turn, position):
    
    detect_piece_color(selected_piece)

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

    if(target_piece != ''):
        print(selected_piece, "->", target_pieces)
    else:
        print(selected_piece, "->", target_square)

    print("New Position:")
    print(position)

    if current_turn == False:
        return True
    else:
        return False 









