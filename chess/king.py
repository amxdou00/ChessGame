from chess.piece import Piece


class King(Piece):
    def __init__(self, color, img, row, col, board):
        super().__init__("king", color, img, row, col, board)

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

        self.moves = moves
