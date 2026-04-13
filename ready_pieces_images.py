from PIL import Image

KING_BLACK = Image.open('./assets/raw_pieces/black-king.png')
KING_WHITE = Image.open('./assets/raw_pieces/white-king.png')
BISHOP_BLACK = Image.open('./assets/raw_pieces/black-bishop.png')
BISHOP_WHITE = Image.open('./assets/raw_pieces/white-bishop.png')
KNIGHT_BLACK = Image.open('./assets/raw_pieces/black-knight.png')
KNIGHT_WHITE = Image.open('./assets/raw_pieces/white-knight.png')
QUEEN_BLACK = Image.open('./assets/raw_pieces/black-queen.png')
QUEEN_WHITE = Image.open('./assets/raw_pieces/white-queen.png')
PAWN_BLACK = Image.open('./assets/raw_pieces/black-pawn.png')
PAWN_WHITE = Image.open('./assets/raw_pieces/white-pawn.png')
ROOK_BLACK = Image.open('./assets/raw_pieces/black-rook.png')
ROOK_WHITE= Image.open('./assets/raw_pieces/white-rook.png')


KING_BLACK= KING_BLACK.resize((90, 90))
KING_WHITE = KING_WHITE.resize((90, 90))
BISHOP_BLACK= BISHOP_BLACK.resize((90, 90))
BISHOP_WHITE= BISHOP_WHITE.resize((90, 90))
KNIGHT_BLACK = KNIGHT_BLACK.resize((90, 90))
KNIGHT_WHITE = KNIGHT_WHITE.resize((90, 90))
PAWN_BLACK = PAWN_BLACK.resize((90, 90))
PAWN_WHITE = PAWN_WHITE.resize((90, 90))
QUEEN_BLACK = QUEEN_BLACK.resize((90, 90))
QUEEN_WHITE = QUEEN_WHITE.resize((90, 90))
ROOK_BLACK = ROOK_BLACK.resize((90, 90))
ROOK_WHITE = ROOK_WHITE.resize((90, 90))

KING_BLACK = KING_BLACK.save('./assets/pieces/black-king.png')
KING_WHITE = KING_WHITE.save('./assets/pieces/white-king.png')
BISHOP_BLACK = BISHOP_BLACK.save('./assets/pieces/black-bishop.png')
BISHOP_WHITE = BISHOP_WHITE.save('./assets/pieces/white-bishop.png')
KNIGHT_BLACK = KNIGHT_BLACK.save('./assets/pieces/black-knight.png')
KNIGHT_WHITE = KNIGHT_WHITE.save('./assets/pieces/white-knight.png')
QUEEN_BLACK = QUEEN_BLACK.save('./assets/pieces/black-queen.png')
QUEEN_WHITE = QUEEN_WHITE.save('./assets/pieces/white-queen.png')
PAWN_BLACK = PAWN_BLACK.save('./assets/pieces/black-pawn.png')
PAWN_WHITE = PAWN_WHITE.save('./assets/pieces/white-pawn.png')
ROOK_BLACK = ROOK_BLACK.save('./assets/pieces/black-rook.png')
ROOK_WHITE= ROOK_WHITE.save('./assets/pieces/white-rook.png')







