import pygame
from game.move import detect_piece_color

def get_pawn_moves(square, color, position, moves):
    Y_index = square[0]
    X_index = square[1]

    print("Current Square: (",Y_index, ', ', X_index, ')') 

    if color == True:
        if Y_index-1 >= 0:
            moves.append([(Y_index-1), (X_index)])
        if Y_index-1 >= 0 and X_index+1 <= 7:
            if position[Y_index-1][X_index+1] != '':
                moves.append([(Y_index-1), (X_index+1)])
        if Y_index-1 >= 0 and X_index-1 >= 0:
            if position[Y_index-1][X_index-1] != '':
                moves.append([(Y_index-1), (X_index-1)])

        print(moves)
        return moves

    if color == False:
        if Y_index+1 <= 7:
            moves.append([(Y_index+1), (X_index)])
        if Y_index+1 <= 7 and X_index+1 <= 7: 
            if position[Y_index+1][X_index+1] != "":
                moves.append([(Y_index+1), (X_index+1)])
        if Y_index+1 <= 7 and X_index-1 >=0: 
            if position[Y_index+1][X_index-1] != "":
                moves.append([(Y_index+1), (X_index-1)])

        print(moves)
        return moves




def get_all_moves(square, piece, position, moves):

    if piece[0] == 'P':
        piece_color = detect_piece_color(piece)
        get_pawn_moves(square, color, position, moves)
        
    
    """For rook moves"""

    if piece == "Rw":
        Y_index_copy = Y_index 
        X_index_copy = X_index
        
        while True:
            if Y_index >= 7:
                break
            if position[Y_index+1][X_index] == '':
                moves.append([(Y_index+1), (X_index)])
                Y_index = Y_index+1
            elif position[Y_index+1][X_index] != '':
                target_piece_color = detect_piece_color(position[Y_index+1][X_index])
                if target_piece_color == False:
                    moves.append([(Y_index+1), (X_index)])
                    break
            else:
                break

        Y_index = Y_index_copy
        X_index = X_index_copy
         
        while True:
            if Y_index <= 0:
                break
            if position[Y_index-1][X_index] == '':
                print("Rook move:", Y_index-1, ", ", X_index)
                moves.append([(Y_index-1),(X_index)])
                Y_index = Y_index-1
            elif position[Y_index-1][X_index] != '':
                target_piece_color = detect_piece_color(position[Y_index-1][X_index])
                if target_piece_color == False:
                    moves.append([(Y_index-1),(X_index)])
                    break
            else:
                break

        Y_index = Y_index_copy
        X_index = X_index_copy
  
        while True:
            if X_index >= 7:
                break
            if position[Y_index][X_index+1] == '':
                moves.append([(Y_index), (X_index+1)])
                X_index = X_index+1
            elif position[Y_index][X_index+1] != '':
                target_piece_color = detect_piece_color(position[Y_index][X_index+1])
                if target_piece_color == False:
                    moves.append([(Y_index), (X_index+1)])
                    break
            else:
                break

        Y_index = Y_index_copy
        X_index = X_index_copy
         
        while True:
            if X_index <= 0:
                break
            if position[Y_index][X_index-1] == '':
                moves.append([(Y_index), (X_index-1)])
                X_index = X_index-1
            elif position[Y_index][X_index-1] != '':
                target_piece_color = detect_piece_color(position[Y_index][X_index-1])
                if target_piece_color == False:
                    moves.append([(Y_index), (X_index-1)])
                    break
            else:
                break

      
        Y_index = Y_index_copy
        X_index = X_index_copy

        print(moves)
        return moves
  


   
    """For bishop moves"""

    """For knight moves"""

    """For king moves"""
    

    return moves

    
