import pygame 
import os

def load_pieces():
    KING_BLACK = pygame.image.load('./assets/pieces/black-king.png').convert_alpha()
    KING_WHITE = pygame.image.load('./assets/pieces/white-king.png').convert_alpha()
    BISHOP_BLACK = pygame.image.load('./assets/pieces/black-bishop.png').convert_alpha()
    BISHOP_WHITE = pygame.image.load('./assets/pieces/white-bishop.png').convert_alpha()
    KNIGHT_BLACK = pygame.image.load('./assets/pieces/black-knight.png').convert_alpha()
    KNIGHT_WHITE = pygame.image.load('./assets/pieces/white-knight.png').convert_alpha()
    QUEEN_BLACK = pygame.image.load('./assets/pieces/black-queen.png').convert_alpha()
    QUEEN_WHITE = pygame.image.load('./assets/pieces/white-queen.png').convert_alpha()
    PAWN_BLACK = pygame.image.load('./assets/pieces/black-pawn.png').convert_alpha()
    PAWN_WHITE = pygame.image.load('./assets/pieces/white-pawn.png').convert_alpha()
    ROOK_BLACK = pygame.image.load('./assets/pieces/black-rook.png').convert_alpha()
    ROOK_WHITE= pygame.image.load('./assets/pieces/white-rook.png').convert_alpha()

    return  [ KING_WHITE, KING_BLACK, ROOK_WHITE, ROOK_BLACK, KNIGHT_WHITE, KNIGHT_BLACK, BISHOP_WHITE, BISHOP_BLACK, QUEEN_WHITE, QUEEN_BLACK, PAWN_WHITE, PAWN_BLACK ]
           
    

def put_piece(surface, piece, square):
    surface.blit(piece, square)
    

def put_pieces(surface, position):
    pieces = load_pieces()
    
    KING_WHITE = pieces[0]
    KING_BLACK = pieces[1]
    ROOK_WHITE = pieces[2]
    ROOK_BLACK = pieces[3]
    KNIGHT_BLACK = pieces[4]
    KNIGHT_WHITE = pieces[5]
    BISHOP_WHITE = pieces[6]
    BISHOP_BLACK = pieces[7]
    QUEEN_WHITE = pieces[8]
    QUEEN_BLACK = pieces[9]
    PAWN_WHITE = pieces[10]
    PAWN_BLACK = pieces[11]

    pieces = {
            "Kw": KING_WHITE,
            "Kb": KING_BLACK,
            "Rw": ROOK_WHITE,
            "Rb": ROOK_BLACK,
            "Nw": KNIGHT_BLACK,
            "Nb": KNIGHT_WHITE,
            "Bw": BISHOP_WHITE,
            "Bb": BISHOP_BLACK,
            "Qw": QUEEN_WHITE,
            "Qb": QUEEN_BLACK,
            "Pw": PAWN_WHITE,
            "Pb": PAWN_BLACK
            }

    piece_left = 0
    piece_top = 0

    for i in range(len(position)):
        for j in range(len(position[i])):
            if position[i][j] != "":
               put_piece(surface, pieces[position[i][j]], (piece_left, piece_top))  
            piece_left = piece_left + 90

        piece_left = 0
        piece_top = piece_top + 90













