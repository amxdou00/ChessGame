
class Piece:
    def __init__(self, name, color, image, row, col, board):
        self.name = name
        self.color = color
        self.image = image
        self.row = row
        self.col = col
        self.moves = []
        self.hasMoved = False
        self.board = board

    def move(self, new_row, new_col):
        self.row = new_row
        self.col = new_col
        self.hasMoved = True

    def delete(self, board):
        self.row = 0
        self.col = 0
        board.remaining_pieces.remove(self)
        board.captured_pieces.append(self)
