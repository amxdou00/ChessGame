
class Game:
    def __init__(self):
        self.is_playing = False
        self.move_logger = []
        self.sides = ["white", "black"]
        self.turn_index = 0
        self.turn = self.sides[self.turn_index]
        self.selected_piece = None

    def start(self):
        self.is_playing = True

    def stop(self):
        self.is_playing = False

    def switch_turn(self):
        self.turn_index = 1 - self.turn_index
        self.turn = self.sides[self.turn_index]

    def log_move(self, piece, start_row, start_col, dest_row, dest_col):
        self.move_logger.append((piece.name, start_row, start_col, dest_row, dest_col))

    def check_endgame(self, board):
        for piece in board.remaining_pieces:
            if piece.color == self.turn and piece.moves != []:
                if '''the king is in check''':
                    pass # checkmate
                else:
                    pass # stalemate



