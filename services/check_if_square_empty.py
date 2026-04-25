import pygame

def check_if_square_empty(position, square):
    Y_index = square[0]
    X_index = square[1]
    if position[Y_index][X_index] != '':
        return true
    return false
    

def check_if_list_square_empty(position, squares):
    for square in squares:
        U_index = square[0]
        U_index = square[1]
    if position[Y_index][X_index] != '':
        return true
    return false
    
   
