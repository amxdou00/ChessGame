from chess.piece import Piece


class King(Piece):
    def __init__(self, color, img, row, col, board):
        super().__init__("king", color, img, row, col, board)

    def is_in_check(self):
        check = False
        for piece in self.board.remaining_pieces:
            if piece.color != self.color:
                if piece.name == "pawn":
                    if piece.color == "white":
                        if self.row == piece.row + 1 and (self.col == piece.col + 1 or self.col == piece.col -1):
                            check = True
                    else:
                        if self.row == piece.row - 1 and (self.col == piece.col + 1 or self.col == piece.col -1):
                            check = True
                else:
                    for move in piece.moves:
                        if move == (self.row, self.col):
                            check = True
                            break

        return check

    def generate_moves(self, game):
        moves = []

        if self.row == 8:
            if self.col == 1:
                if self.board.piece_at_case(self.row, self.col + 1) is None or self.board.piece_at_case(self.row,
                                                                                                        self.col + 1).color != self.color:
                    moves.append((self.row, self.col + 1))

                if self.board.piece_at_case(self.row - 1, self.col + 1) is None or self.board.piece_at_case(
                        self.row - 1,
                        self.col + 1).color != self.color:
                    moves.append((self.row - 1, self.col + 1))

                if self.board.piece_at_case(self.row - 1, self.col) is None or self.board.piece_at_case(self.row - 1,
                                                                                                        self.col).color != self.color:
                    moves.append((self.row - 1, self.col))

            if self.col == 8:
                if self.board.piece_at_case(self.row, self.col - 1) is None or self.board.piece_at_case(self.row,
                                                                                                        self.col - 1).color != self.color:
                    moves.append((self.row, self.col - 1))

                if self.board.piece_at_case(self.row - 1, self.col - 1) is None or self.board.piece_at_case(
                        self.row - 1,
                        self.col - 1).color != self.color:
                    moves.append((self.row - 1, self.col - 1))

                if self.board.piece_at_case(self.row - 1, self.col) is None or self.board.piece_at_case(self.row - 1,
                                                                                                        self.col).color != self.color:
                    moves.append((self.row - 1, self.col))

            if self.col != 1 and self.col != 8:
                if self.board.piece_at_case(self.row, self.col + 1) is None or self.board.piece_at_case(self.row,
                                                                                                        self.col + 1).color != self.color:
                    moves.append((self.row, self.col + 1))

                if self.board.piece_at_case(self.row - 1, self.col + 1) is None or self.board.piece_at_case(
                        self.row - 1,
                        self.col + 1).color != self.color:
                    moves.append((self.row - 1, self.col + 1))

                if self.board.piece_at_case(self.row - 1, self.col) is None or self.board.piece_at_case(self.row - 1,
                                                                                                        self.col).color != self.color:
                    moves.append((self.row - 1, self.col))

                if self.board.piece_at_case(self.row - 1, self.col - 1) is None or self.board.piece_at_case(
                        self.row - 1,
                        self.col - 1).color != self.color:
                    moves.append((self.row - 1, self.col - 1))

                if self.board.piece_at_case(self.row, self.col - 1) is None or self.board.piece_at_case(self.row,
                                                                                                        self.col - 1).color != self.color:
                    moves.append((self.row, self.col - 1))

        elif self.row == 1:
            if self.col == 1:
                if self.board.piece_at_case(self.row + 1, self.col) is None or self.board.piece_at_case(self.row + 1,
                                                                                                        self.col).color != self.color:
                    moves.append((self.row + 1, self.col))

                if self.board.piece_at_case(self.row + 1, self.col + 1) is None or self.board.piece_at_case(
                        self.row + 1,
                        self.col + 1).color != self.color:
                    moves.append((self.row + 1, self.col + 1))

                if self.board.piece_at_case(self.row, self.col + 1) is None or self.board.piece_at_case(self.row,
                                                                                                        self.col + 1).color != self.color:
                    moves.append((self.row, self.col + 1))

            if self.col == 8:
                if self.board.piece_at_case(self.row + 1, self.col) is None or self.board.piece_at_case(self.row + 1,
                                                                                                        self.col).color != self.color:
                    moves.append((self.row + 1, self.col))

                if self.board.piece_at_case(self.row + 1, self.col - 1) is None or self.board.piece_at_case(
                        self.row + 1,
                        self.col - 1).color != self.color:
                    moves.append((self.row + 1, self.col - 1))

                if self.board.piece_at_case(self.row, self.col - 1) is None or self.board.piece_at_case(self.row,
                                                                                                        self.col - 1).color != self.color:
                    moves.append((self.row, self.col - 1))

            if self.col != 1 and self.col != 8:
                if self.board.piece_at_case(self.row, self.col + 1) is None or self.board.piece_at_case(self.row,
                                                                                                        self.col + 1).color != self.color:
                    moves.append((self.row, self.col + 1))

                if self.board.piece_at_case(self.row, self.col - 1) is None or self.board.piece_at_case(self.row,
                                                                                                        self.col - 1).color != self.color:
                    moves.append((self.row, self.col - 1))

                if self.board.piece_at_case(self.row + 1, self.col) is None or self.board.piece_at_case(self.row + 1,
                                                                                                        self.col).color != self.color:
                    moves.append((self.row + 1, self.col))

                if self.board.piece_at_case(self.row + 1, self.col + 1) is None or self.board.piece_at_case(
                        self.row + 1,
                        self.col + 1).color != self.color:
                    moves.append((self.row + 1, self.col + 1))

                if self.board.piece_at_case(self.row + 1, self.col - 1) is None or self.board.piece_at_case(
                        self.row + 1,
                        self.col - 1).color != self.color:
                    moves.append((self.row + 1, self.col - 1))

        elif self.col == 8:
            if self.row != 1 and self.row != 8:
                if self.board.piece_at_case(self.row + 1, self.col) is None or self.board.piece_at_case(self.row + 1,
                                                                                                        self.col).color != self.color:
                    moves.append((self.row + 1, self.col))

                if self.board.piece_at_case(self.row - 1, self.col) is None or self.board.piece_at_case(self.row - 1,
                                                                                                        self.col).color != self.color:
                    moves.append((self.row - 1, self.col))

                if self.board.piece_at_case(self.row, self.col - 1) is None or self.board.piece_at_case(self.row,
                                                                                                        self.col - 1).color != self.color:
                    moves.append((self.row, self.col - 1))

                if self.board.piece_at_case(self.row - 1, self.col - 1) is None or self.board.piece_at_case(
                        self.row - 1,
                        self.col - 1).color != self.color:
                    moves.append((self.row - 1, self.col - 1))

                if self.board.piece_at_case(self.row + 1, self.col - 1) is None or self.board.piece_at_case(
                        self.row + 1,
                        self.col - 1).color != self.color:
                    moves.append((self.row + 1, self.col - 1))

        elif self.col == 1:
            if self.row != 1 and self.row != 8:
                if self.board.piece_at_case(self.row + 1, self.col) is None or self.board.piece_at_case(self.row + 1,
                                                                                                        self.col).color != self.color:
                    moves.append((self.row + 1, self.col))

                if self.board.piece_at_case(self.row - 1, self.col) is None or self.board.piece_at_case(self.row - 1,
                                                                                                        self.col).color != self.color:
                    moves.append((self.row - 1, self.col))

                if self.board.piece_at_case(self.row, self.col + 1) is None or self.board.piece_at_case(self.row,
                                                                                                        self.col + 1).color != self.color:
                    moves.append((self.row, self.col + 1))

                if self.board.piece_at_case(self.row + 1, self.col + 1) is None or self.board.piece_at_case(
                        self.row + 1,
                        self.col + 1).color != self.color:
                    moves.append((self.row + 1, self.col + 1))

                if self.board.piece_at_case(self.row - 1, self.col + 1) is None or self.board.piece_at_case(
                        self.row - 1,
                        self.col + 1).color != self.color:
                    moves.append((self.row - 1, self.col + 1))

        else:
            if self.board.piece_at_case(self.row + 1, self.col) is None or self.board.piece_at_case(self.row + 1,
                                                                                                    self.col).color != self.color:
                moves.append((self.row + 1, self.col))

            if self.board.piece_at_case(self.row - 1, self.col) is None or self.board.piece_at_case(self.row - 1,
                                                                                                    self.col).color != self.color:
                moves.append((self.row - 1, self.col))

            if self.board.piece_at_case(self.row, self.col + 1) is None or self.board.piece_at_case(self.row,
                                                                                                    self.col + 1).color != self.color:
                moves.append((self.row, self.col + 1))

            if self.board.piece_at_case(self.row, self.col - 1) is None or self.board.piece_at_case(self.row,
                                                                                                    self.col - 1).color != self.color:
                moves.append((self.row, self.col - 1))

            if self.board.piece_at_case(self.row + 1, self.col + 1) is None or self.board.piece_at_case(self.row + 1,
                                                                                                        self.col + 1).color != self.color:
                moves.append((self.row + 1, self.col + 1))

            if self.board.piece_at_case(self.row - 1, self.col - 1) is None or self.board.piece_at_case(self.row - 1,
                                                                                                        self.col - 1).color != self.color:
                moves.append((self.row - 1, self.col - 1))

            if self.board.piece_at_case(self.row + 1, self.col - 1) is None or self.board.piece_at_case(self.row + 1,
                                                                                                        self.col - 1).color != self.color:
                moves.append((self.row + 1, self.col - 1))

            if self.board.piece_at_case(self.row - 1, self.col + 1) is None or self.board.piece_at_case(self.row - 1,
                                                                                                        self.col + 1).color != self.color:
                moves.append((self.row - 1, self.col + 1))

        if not self.is_in_check():
            # Short castle
            if not self.hasMoved:
                if self.board.piece_at_case(self.row, self.col + 1) is None and self.board.piece_at_case(self.row, self.col + 2) is None:
                    if self.board.piece_at_case(self.row, self.col + 3) is not None and not self.board.piece_at_case(self.row, self.col + 3).hasMoved:
                        if self.board.is_square_safe_for(self.color, self.row, self.col + 1) and self.board.is_square_safe_for(self.color, self.row, self.col + 2):
                            moves.append((self.row, self.col + 2))
            
            # Long castle
            if not self.hasMoved:
                if self.board.piece_at_case(self.row, self.col - 1) is None and self.board.piece_at_case(self.row, self.col - 2) is None and self.board.piece_at_case(self.row, self.col - 3) is None:
                    if self.board.piece_at_case(self.row, self.col - 4) is not None and not self.board.piece_at_case(self.row, self.col - 4).hasMoved:
                        if self.board.is_square_safe_for(self.color, self.row, self.col - 1) and self.board.is_square_safe_for(self.color, self.row, self.col - 2) and self.board.is_square_safe_for(self.color, self.row, self.col - 3):
                            moves.append((self.row, self.col - 2))

        self.moves = moves

    def move(self, new_row, new_col):
        if new_col == self.col + 2:
            self.board.piece_at_case(self.row, self.col + 3).move(self.row, self.col + 1)
        if new_col == self.col - 2:
            self.board.piece_at_case(self.row, self.col - 4).move(self.row, self.col - 1)

        self.row = new_row
        self.col = new_col
        self.hasMoved = True