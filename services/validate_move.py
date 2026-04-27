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
    print("=== Checking Pawn Move Validity ===")
    if color == True:
        if Y_index_target != Y_index_piece - 1:
            return False, "[Invalid Move]: Pawns Must Move Forward"

        if X_index_target != X_index_piece:
            if target_piece != '' and is_take_possible:
                return True, '[Valid Move]: Taking By Pawn'
            else:
                return False, '[Invalid Move]: Attacking your own piece or Wrong Pawn Move, i.e. Diagnol while not attacking'
        else:
            if target_piece != '':
                return False, '[Invalid Move]: Pawns Cannot Attack Piece Straight Infront' 
            else:
                return True, '[Valid Move]: Pushing Pawn'

            


    if color == False:
        if Y_index_target != Y_index_piece + 1:
            return False, "[Invalid Move]: Pawns Must Move Forward"

        if X_index_target != X_index_piece:
            if target_piece != '' and is_take_possible:
                return True, '[Valid Move]: Taking By Pawn'
            else:
                return False, '[Invalid Move]: Attacking your own piece or Wrong Pawn Move, i.e. Diagnol while not attacking'
        else:
            if target_piece != '':
                return False, '[Invalid Move]: Pawns Cannot Attack Piece Straight Infront' 
            else:
                return True, '[Valid Move]: Pushing Pawns'


def is_legal_rook_move(Y_index_piece, X_index_piece, Y_index_target, X_index_target, target_piece, position, piece_color, take_possible):
    print("=== Checking Rook Move Validity ===")
    if X_index_piece == X_index_target:
        if Y_index_piece == Y_index_target:
            return False, "[Invalid Move]: Not To The Same Square You Moronnnnnn!"

    if X_index_piece != X_index_target and Y_index_piece != Y_index_target:
        print("Here")
        return False, "[Invalid Move]: Rooks Can only Move Vertically or Horizontally Straight"
    
    if take_possible == False:
        return False, "[Invalid Move]: Cannot Take Your Own Piece"

    if X_index_piece == X_index_target and Y_index_target < Y_index_piece:
        Y_index_piece_copy = Y_index_piece
        while Y_index_target + 1 < Y_index_piece_copy - 1:
            Y_index_piece_copy = Y_index_piece_copy - 1
            if position[Y_index_piece_copy][X_index_piece] != '':
                print("(", Y_index_piece_copy, " ," ,X_index_piece, "): ", position[Y_index_piece_copy][X_index_piece], " In The  Way")
                return False, '[Invalid Move]: Something In The Wayy'

    if X_index_piece == X_index_target and Y_index_target > Y_index_piece:
        Y_index_piece_copy = Y_index_piece
        while Y_index_target - 1> Y_index_piece_copy:
            Y_index_piece_copy = Y_index_piece_copy + 1
            if position[Y_index_piece_copy][X_index_piece] != '':
                print("(", Y_index_piece_copy, " ," ,X_index_piece, "): ", position[Y_index_piece_copy][X_index_piece], " In The  Way")
                return False, '[Invalid Move]: Something In The Wayy'

    if Y_index_piece == Y_index_target and X_index_target < X_index_piece:
        X_index_piece_copy = X_index_piece
        while X_index_target + 1 < X_index_piece_copy:
            X_index_piece_copy = X_index_piece_copy - 1
            if position[Y_index_piece][X_index_piece_copy] != '':
                return False, '[Invalid Move]: Something In The Wayy'

    if Y_index_piece == Y_index_target and X_index_target > X_index_piece:
        X_index_piece_copy = X_index_piece
        while X_index_target - 1 > X_index_piece_copy:
            X_index_piece_copy = X_index_piece_copy + 1
            if position[Y_index_piece][X_index_piece_copy] != '':
                print(X_index_target, ">", X_index_piece_copy)
                return False, '[Invalid Move]: Something In The Wayy'

    if target_piece != '' and take_possible == True:
        return True, '[Valid Move]: Taking With The Rooooooooooook! '

    if target_piece == '':
        return True, "[Valid Move]: Moving Your Rook Somewhere, Noice"


def is_legal_knight_move(Y_index_piece, X_index_piece, Y_index_target, X_index_target, target_piece, position, piece_color, take_possible):
    if target_piece != '' and take_possible == False:
        return False, '[Invalid Move]: Cannot Take Your Own Piece'

    if X_index_target - X_index_piece == 2 or X_index_target - X_index_piece == -2:
        if Y_index_target - Y_index_piece == 1 or Y_index_target - Y_index_piece == -1:
            if target_piece == '':
                return True, '[Valid Move]: Valid Knight Move'

            if target_piece != '' and take_possible == True:
                return True, '[Valid Move]: Yeahh Taking With The Knight'

    if Y_index_target - Y_index_piece == 2 or Y_index_target - Y_index_piece == -2:
        if X_index_target - X_index_piece == 1 or X_index_target - X_index_piece == -1:
            if target_piece == '':
                return True, '[Valid Move]: Valid Knight Move'

            if target_piece != '' and take_possible == True:
                return True, '[Valid Move]: Yeahh Taking With The Knight'

    return False, '[Invalid Move]: You Moron! Know That The Knight Moves in L Shape'



            
def is_move_valid(piece, square, position, target_square):
    Y_index_piece = square[0]
    X_index_piece = square[1]

    Y_index_target = target_square[0]
    X_index_target = target_square[1]

    target_piece = position[Y_index_target][X_index_target]

    piece_color = detect_piece_color(piece)
    target_color = False if piece_color == True else True
    take_possible = True 
    if target_piece != '':
        target_color = detect_piece_color(target_piece)
        take_possible = is_take_possible(piece_color, target_color)


    if piece[0] == 'P':
        validity, message = is_legal_pawn_move(Y_index_piece, X_index_piece, Y_index_target, X_index_target, target_piece, position, piece_color, take_possible)
        print(message)
        return validity

    if piece[0] == 'R':
        validity, message = is_legal_rook_move(Y_index_piece, X_index_piece, Y_index_target, X_index_target, target_piece, position, piece_color, take_possible)
        print(message)
        return validity

    if piece[0] == 'N':
        validity, message = is_legal_knight_move(Y_index_piece, X_index_piece, Y_index_target, X_index_target, target_piece, position, piece_color, take_possible)
        print(message)
        return validity

















