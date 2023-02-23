from chess.piece import Piece
from chess.queen import Queen
from chess.constants import wqueen_img, bqueen_img

class Pawn(Piece):
    def __init__(self, color, image, row, col, board):
        super().__init__("pawn", color, image, row, col, board)
        self.en_passant_possible = False

    def generate_moves(self, game):
        moves = []

        # Two squares move
        if self.color == "white":
            if not self.hasMoved and self.board.piece_at_case(self.row + 2, self.col) is None:
                moves.append((self.row + 2, self.col))
        if self.color == "black":
            if not self.hasMoved and self.board.piece_at_case(self.row - 2, self.col) is None:
                moves.append((self.row - 2, self.col))

        # Regular one square forward move
        if self.color == "white" and self.board.piece_at_case(self.row + 1, self.col) is None:
            moves.append((self.row + 1, self.col))
        if self.color == "black" and self.board.piece_at_case(self.row - 1, self.col) is None:
            moves.append((self.row - 1, self.col))

        # Capturing move
        if self.color == "white":
            if self.board.piece_at_case(self.row + 1, self.col + 1) is not None:
                if self.board.piece_at_case(self.row + 1, self.col + 1).color == "black":
                    moves.append((self.row + 1, self.col + 1))

            if self.board.piece_at_case(self.row + 1, self.col - 1) is not None:
                if self.board.piece_at_case(self.row + 1, self.col - 1).color == "black":
                    moves.append((self.row + 1, self.col - 1))

        if self.color == "black":
            if self.board.piece_at_case(self.row - 1, self.col + 1) is not None:
                if self.board.piece_at_case(self.row - 1, self.col + 1).color == "white":
                    moves.append((self.row - 1, self.col + 1))

            if self.board.piece_at_case(self.row - 1, self.col - 1) is not None:
                if self.board.piece_at_case(self.row - 1, self.col - 1).color == "white":
                    moves.append((self.row - 1, self.col - 1))

        # En passant
        if self.color == "white":
            if self.row == 5:
                if self.board.piece_at_case(self.row, self.col + 1) is not None:
                    if self.board.piece_at_case(self.row, self.col + 1).color == "black":
                        last_move_piece = game.move_logger[-1][0]
                        last_move_start_row = game.move_logger[-1][1]
                        last_move_dest_row = game.move_logger[-1][3]
                        last_move_dest_col = game.move_logger[-1][4]

                        if last_move_piece == "pawn":
                            if abs(last_move_dest_row - last_move_start_row) == 2 and last_move_dest_row == self.row:
                                if last_move_dest_col == self.col + 1:
                                    moves.append((self.row + 1, self.col + 1))
                                    self.en_passant_possible = True

                if self.board.piece_at_case(self.row, self.col - 1) is not None:
                    if self.board.piece_at_case(self.row, self.col - 1).color == "black":
                        last_move_piece = game.move_logger[-1][0]
                        last_move_start_row = game.move_logger[-1][1]
                        last_move_dest_row = game.move_logger[-1][3]
                        last_move_dest_col = game.move_logger[-1][4]

                        if last_move_piece == "pawn":
                            if abs(last_move_dest_row - last_move_start_row) == 2 and last_move_dest_row == self.row:
                                if last_move_dest_col == self.col - 1:
                                    moves.append((self.row + 1, self.col - 1))
                                    self.en_passant_possible = True

        else:
            if self.row == 4:
                if self.board.piece_at_case(self.row, self.col + 1) is not None:
                    if self.board.piece_at_case(self.row, self.col + 1).color == "white":
                        last_move_piece = game.move_logger[-1][0]
                        last_move_start_row = game.move_logger[-1][1]
                        last_move_dest_row = game.move_logger[-1][3]
                        last_move_dest_col = game.move_logger[-1][4]

                        if last_move_piece == "pawn":
                            if abs(last_move_dest_row - last_move_start_row) == 2 and last_move_dest_row == self.row:
                                if last_move_dest_col == self.col + 1:
                                    moves.append((self.row - 1, self.col + 1))
                                    self.en_passant_possible = True

                if self.board.piece_at_case(self.row, self.col - 1) is not None:
                    if self.board.piece_at_case(self.row, self.col - 1).color == "white":
                        last_move_piece = game.move_logger[-1][0]
                        last_move_start_row = game.move_logger[-1][1]
                        last_move_dest_row = game.move_logger[-1][3]
                        last_move_dest_col = game.move_logger[-1][4]

                        if last_move_piece == "pawn":
                            if abs(last_move_dest_row - last_move_start_row) == 2 and last_move_dest_row == self.row:
                                if last_move_dest_col == self.col - 1:
                                    moves.append((self.row - 1, self.col - 1))
                                    self.en_passant_possible = True

        # Promotion
        if self.color == "white" and self.row == 8:
            save_row = self.row
            save_col = self.col
            self.delete(self.board)
            new_white_queen = Queen("white", wqueen_img, save_row, save_col, self.board)
            self.board.remaining_pieces.append(new_white_queen)
            self.board.update(game)
        if self.color ==  "black" and self.row == 1:
            save_row = self.row
            save_col = self.col
            self.delete(self.board)
            new_black_queen = Queen("black", bqueen_img, save_row, save_col, self.board)
            self.board.remaining_pieces.append(new_black_queen)
            self.board.update(game)

        self.moves = moves

    def move(self, new_row, new_col):
        if self.color == "white" and self.row == 5:
            if new_row == self.row + 1 and new_col == self.col + 1 and self.en_passant_possible:
                self.board.piece_at_case(self.row, self.col + 1).delete(self.board)
            if new_row == self.row + 1 and new_col == self.col - 1 and self.en_passant_possible:
                self.board.piece_at_case(self.row, self.col - 1).delete(self.board)

        elif self.color == "black" and self.row == 4:
            if new_row == self.row - 1 and new_col == self.col + 1 and self.en_passant_possible:
                self.board.piece_at_case(self.row, self.col + 1).delete(self.board)
            if new_row == self.row - 1 and new_col == self.col - 1 and self.en_passant_possible:
                self.board.piece_at_case(self.row, self.col - 1).delete(self.board)

        self.row = new_row
        self.col = new_col
        self.hasMoved = True
