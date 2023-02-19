from chess.piece import Piece


class Bishop(Piece):
    def __init__(self, color, img, row, col, board):
        super().__init__("bishop", color, img, row, col, board)

    def generate_moves(self, game):
        moves = []

        # Adding all the possible moves
        for i in range(1, min(self.board.ROWS - self.row + 1, self.board.COLS - self.col + 1)):
            if self.board.piece_at_case(self.row + i, self.col + i) is None or self.board.piece_at_case(self.row + i,
                                                                                  self.col + i).color != self.color:
                moves.append((self.row + i, self.col + i))
            else:
                break

        for i in range(1, min(self.board.ROWS - self.row + 1, self.col - 1 + 1)):
            if self.board.piece_at_case(self.row + i, self.col - i) is None or self.board.piece_at_case(self.row + i,
                                                                                  self.col - i).color != self.color:
                moves.append((self.row + i, self.col - i))
            else:
                break

        for i in range(1, min(self.board.COLS - self.col + 1, self.row - 1 + 1)):
            if self.board.piece_at_case(self.row - i, self.col + i) is None or self.board.piece_at_case(self.row - i,
                                                                                  self.col + i).color != self.color:
                moves.append((self.row - i, self.col + i))
            else:
                break

        for i in range(1, min(self.row - 1 + 1, self.col - 1 + 1)):
            if self.board.piece_at_case(self.row - i, self.col - i) is None or self.board.piece_at_case(self.row - i,
                                                                                  self.col - i).color != self.color:
                moves.append((self.row - i, self.col - i))
            else:
                break

        self.moves = moves
