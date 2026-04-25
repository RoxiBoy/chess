from game.move import detect_piece_color
from services.get_all_possible_moves import get_all_moves

def validate_move(position, selected_piece, selected_square, target_piece, target_square):
    is_attack = False
    print('Selected Square', selected_square)
    print('Targetet Square: ', target_square)
    print('Selected Piece: ', selected_piece)
    print('Targetted Piece: ', target_piece)

    all_moves = get_all_moves(selected_square, selected_piece, position)
    print("All moves for :", selected_piece, ': ', all_moves)

    if target_square in all_moves:
        return True
    else:
        print("[Invalid Move] Cannot Move Rhat Piece There")
    if target_piece == '':
        is_attack = False
    moving_piece_color = detect_piece_color(selected_piece)

    if is_attack == True: 
        target_piece_color = detect_piece_color(target_piece)
        if moving_piece_color == target_piece_color:
            print("Invalid Move: Taking your own piece")
            return False

def is_take_possible(color1, color2):
    if color1 == color2:
        return False
    else:
        return True

def is_legal_pawn_move(Y_index_piece, X_index_piece, Y_index_target, X_index_target, target_piece, position, color, is_take_possible):
    if color = True:
        if Y_index_target != Y_index_piece - 1:
            return False

        if X_index_target != X_index_piece:
            if target_piece != '' and is_take_possible:
                return True 
            else:
                return False 
        else:
            if target_piece != '' and is_take_possible:
                return False 
            else:
                return True

            


    if color = False:
        if Y_index_target != Y_index_piece + 1:
            return False


        if X_index_target != X_index_piece:
            if target_piece != '' and is_take_possible:
                return True 
            else:
                return False 
        else:
            if target_piece != '' and is_take_possible:
                return False 
            else:
                return True


def is_move_valid(piece, square, position, target_square)
    Y_index_piece = square[0]
    X_index_piece = square[1]

    Y_index_target = target_square[0]
    X_index_target = target_square[1]

    target_piece = position[Y_index_target][X_index_target]

    piece_color = detect_piece_color(piece)
    target_color = detect_piece_color(color)

    is_take_possible = is_take_possible(piece_color, target_color)

    if piece[0] == 'P':
        return is_legal_pawn_move(Y_index_piece, X_index_piece, Y_index_target, X_index_target, target_piece, position, piece_color, is_take_possible)















