from chess.piece import Piece


class Queen(Piece):
    def __init__(self, color, img, row, col, board):
        super().__init__("queen", color, img, row, col, board)

    def generate_moves(self, game):
        moves = []
        for i in range(1, self.board.ROWS - self.row + 1):
            if self.board.piece_at_case(self.row + i, self.col) is None:
                moves.append((self.row + i, self.col))
            else:
                if self.color != self.board.piece_at_case(self.row + i, self.col).color:
                    moves.append((self.row + i, self.col))
                    break
                else:
                    break

        for i in range(1, self.row - 1 + 1):
            if self.board.piece_at_case(self.row - i, self.col) is None:
                moves.append((self.row - i, self.col))
            else:
                if self.color != self.board.piece_at_case(self.row - i, self.col).color:
                    moves.append((self.row - i, self.col))
                    break
                else:
                    break

        for i in range(1, self.board.COLS - self.col + 1):
            if self.board.piece_at_case(self.row, self.col + i) is None:
                moves.append((self.row, self.col + i))
            else:
                if self.color != self.board.piece_at_case(self.row, self.col + i).color:
                    moves.append((self.row, self.col + i))
                    break
                else:
                    break

        for i in range(1, self.col - 1 + 1):
            if self.board.piece_at_case(self.row, self.col - i) is None:
                moves.append((self.row, self.col - i))
            else:
                if self.color != self.board.piece_at_case(self.row, self.col - i).color:
                    moves.append((self.row, self.col - i))
                    break
                else:
                    break

        for i in range(1, min(self.board.ROWS - self.row + 1, self.board.COLS - self.col + 1)):
            if self.board.piece_at_case(self.row + i, self.col + i) is None:
                moves.append((self.row + i, self.col + i))
            else:
                if self.color != self.board.piece_at_case(self.row + i, self.col + i).color:
                    moves.append((self.row + i, self.col + i))
                    break
                else:
                    break

        for i in range(1, min(self.board.ROWS - self.row + 1, self.col - 1 + 1)):
            if self.board.piece_at_case(self.row + i, self.col - i) is None:
                moves.append((self.row + i, self.col - i))
            else:
                if self.color != self.board.piece_at_case(self.row + i, self.col - i).color:
                    moves.append((self.row + i, self.col - i))
                    break
                else:
                    break

        for i in range(1, min(self.board.COLS - self.col + 1, self.row - 1 + 1)):
            if self.board.piece_at_case(self.row - i, self.col + i) is None:
                moves.append((self.row - i, self.col + i))
            else:
                if self.color != self.board.piece_at_case(self.row - i, self.col + i).color:
                    moves.append((self.row - i, self.col + i))
                    break
                else:
                    break

        for i in range(1, min(self.row - 1 + 1, self.col - 1 + 1)):
            if self.board.piece_at_case(self.row - i, self.col - i) is None:
                moves.append((self.row - i, self.col - i))
            else:
                if self.color != self.board.piece_at_case(self.row - i, self.col - i).color:
                    moves.append((self.row - i, self.col - i))
                    break
                else:
                    break

        self.moves = moves
