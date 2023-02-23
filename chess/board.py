import pygame as pygame

from chess.bishop import Bishop
from chess.constants import wpawn_img, bpawn_img, piece_size, wknight_img, bknight_img, wbishop_img, bbishop_img, \
    bqueen_img, wqueen_img, bking_img, wking_img, wrook_img, brook_img
from chess.king import King
from chess.knight import Knight
from chess.pawn import Pawn
from chess.queen import Queen
from chess.rook import Rook


class Board:
    def __init__(self, size, screen):
        self.ROWS = self.COLS = 8
        self.size = size
        self.square_size = self.size / self.ROWS
        self.screen = screen
        self.remaining_pieces = []
        self.captured_pieces = []

    def create_pieces(self):

        wpawn1 = Pawn("white", wpawn_img, 2, 1, self)
        wpawn2 = Pawn("white", wpawn_img, 2, 2, self)
        wpawn3 = Pawn("white", wpawn_img, 2, 3, self)
        wpawn4 = Pawn("white", wpawn_img, 2, 4, self)
        wpawn5 = Pawn("white", wpawn_img, 2, 5, self)
        wpawn6 = Pawn("white", wpawn_img, 2, 6, self)
        wpawn7 = Pawn("white", wpawn_img, 2, 7, self)
        wpawn8 = Pawn("white", wpawn_img, 2, 8, self)
        wknight1 = Knight("white", wknight_img, 1, 2, self)
        wknight2 = Knight("white", wknight_img, 1, 7, self)
        wbishop1 = Bishop("white", wbishop_img, 1, 3, self)
        wbishop2 = Bishop("white", wbishop_img, 1, 6, self)
        wrook1 = Rook("white", wrook_img, 1, 1, self)
        wrook2 = Rook("white", wrook_img, 1, 8, self)
        wqueen = Queen("white", wqueen_img, 1, 4, self)
        wking = King("white", wking_img, 1, 5, self)

        bpawn1 = Pawn("black", bpawn_img, 7, 1, self)
        bpawn2 = Pawn("black", bpawn_img, 7, 2, self)
        bpawn3 = Pawn("black", bpawn_img, 7, 3, self)
        bpawn4 = Pawn("black", bpawn_img, 7, 4, self)
        bpawn5 = Pawn("black", bpawn_img, 7, 5, self)
        bpawn6 = Pawn("black", bpawn_img, 7, 6, self)
        bpawn7 = Pawn("black", bpawn_img, 7, 7, self)
        bpawn8 = Pawn("black", bpawn_img, 7, 8, self)
        bknight1 = Knight("black", bknight_img, 8, 2, self)
        bknight2 = Knight("black", bknight_img, 8, 7, self)
        bbishop1 = Bishop("black", bbishop_img, 8, 3, self)
        bbishop2 = Bishop("black", bbishop_img, 8, 6, self)
        brook1 = Rook("black", brook_img, 8, 1, self)
        brook2 = Rook("black", brook_img, 8, 8, self)
        bqueen = Queen("black", bqueen_img, 8, 4, self)
        bking = King("black", bking_img, 8, 5, self)

        self.remaining_pieces = [
            wpawn1, wpawn2, wpawn3, wpawn4, wpawn5, wpawn6, wpawn7, wpawn8,
            wknight1, wknight2, wbishop1, wbishop2, wrook1, wrook2, wqueen, wking,
            bpawn1, bpawn2, bpawn3, bpawn4, bpawn5, bpawn6, bpawn7, bpawn8,
            bknight1, bknight2, bbishop1, bbishop2, brook1, brook2, bqueen, bking
        ]

    def draw_board(self, dark_color, light_color):
        colors = [light_color, dark_color]

        for row in range(self.ROWS):
            for col in range(self.COLS):
                square_rect = pygame.Rect(
                    col * self.square_size, row * self.square_size, self.square_size, self.square_size
                )
                square_color = colors[(row+col) % 2]
                pygame.draw.rect(self.screen, square_color, square_rect)

    def draw_pieces(self):
        for piece in self.remaining_pieces:
            blit_coordinate = (
                (piece.col - 1) * self.square_size + (self.square_size / 2 - piece_size[0] / 2),
                (((self.ROWS - piece.row) * self.square_size) + (self.square_size / 2 - piece_size[0] / 2))
            )
            self.screen.blit(piece.image, blit_coordinate)

        pygame.display.update()

    def update_pieces(self, game):
        for piece in self.remaining_pieces:
            piece.generate_moves(game)

    def update(self, game):
        # Redrawing the board and the pieces
        self.draw_board(pygame.Color(178, 138, 98), pygame.Color(250, 217, 184))
        self.draw_pieces()
        # Updating the moves for each piece
        for piece in self.remaining_pieces:
            if piece.name == "pawn":
                piece.en_passant_possible = False
            piece.generate_moves(game)

    def piece_at_case(self, row, col):
        for piece in self.remaining_pieces:
            if piece.row == row and piece.col == col:
                return piece

    def init(self, game):
        # Drawing the board
        self.draw_board(pygame.Color(178, 138, 98), pygame.Color(250, 217, 184))
        # Creating the pieces
        self.create_pieces()
        # Drawing the pieces
        self.draw_pieces()
        # Updating the pieces
        self.update_pieces(game)

    def is_square_safe_for(self, color, row, col):
        safe = True
        for piece in self.remaining_pieces:
            if piece.color != color:
                for move in piece.moves:
                    if move == (row, col):
                        safe = False
                        break
        return safe
    
