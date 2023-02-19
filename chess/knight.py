from chess.piece import Piece


class Knight(Piece):
    def __init__(self, color, image, row, col, board):
        super().__init__("knight", color, image, row, col, board)

    def generate_moves(self, game):
        moves = []
        if self.row + 2 <= 8 and self.col + 1 <= 8:
            if self.board.piece_at_case(self.row + 2, self.col + 1) is None or self.board.piece_at_case(self.row + 2,
                                                                                                        self.col + 1).color != self.color:
                moves.append((self.row + 2, self.col + 1))

        if self.row + 1 <= 8 and self.col + 2 <= 8:
            if self.board.piece_at_case(self.row + 1, self.col + 2) is None or self.board.piece_at_case(self.row + 1,
                                                                                                        self.col + 2).color != self.color:
                moves.append((self.row + 1, self.col + 2))

        if self.row - 1 >= 1 and self.col + 2 <= 8:
            if self.board.piece_at_case(self.row - 1, self.col + 2) is None or self.board.piece_at_case(self.row - 1,
                                                                                                        self.col + 2).color != self.color:
                moves.append((self.row - 1, self.col + 2))

        if self.row - 2 >= 1 and self.col + 1 <= 8:
            if self.board.piece_at_case(self.row - 2, self.col + 1) is None or self.board.piece_at_case(self.row - 2,
                                                                                                        self.col + 1).color != self.color:
                moves.append((self.row - 2, self.col + 1))

        if self.row - 2 >= 1 and self.col - 1 >= 1:
            if self.board.piece_at_case(self.row - 2, self.col - 1) is None or self.board.piece_at_case(self.row - 2,
                                                                                                        self.col - 1).color != self.color:
                moves.append((self.row - 2, self.col - 1))

        if self.row - 1 >= 1 and self.col - 2 >= 1:
            if self.board.piece_at_case(self.row - 1, self.col - 2) is None or self.board.piece_at_case(self.row - 1,
                                                                                                        self.col - 2).color != self.color:
                moves.append((self.row - 1, self.col - 2))

        if self.row + 1 <= 8 and self.col - 2 >= 1:
            if self.board.piece_at_case(self.row + 1, self.col - 2) is None or self.board.piece_at_case(self.row + 1,
                                                                                                        self.col - 2).color != self.color:
                moves.append((self.row + 1, self.col - 2))

        if self.row + 2 <= 8 and self.col - 1 >= 1:
            if self.board.piece_at_case(self.row + 2, self.col - 1) is None or self.board.piece_at_case(self.row + 2,
                                                                                                        self.col - 1).color != self.color:
                moves.append((self.row + 2, self.col - 1))

        self.moves = moves
