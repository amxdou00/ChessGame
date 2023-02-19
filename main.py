import pygame

from chess.board import Board
from chess.constants import WINDOW_SIZE, dot_size, greendot_img
from chess.game import Game


# Initializing pygame
pygame.init()

# Creating the game window
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Chess Game")

# Creating the game object
game = Game()

# Starting the game
game.start()

# Creating and initializing the board
board = Board(WINDOW_SIZE, window)
board.init(game)

# Game loop
while game.is_playing:

    #print(game.move_logger)

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.stop()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Getting the mouse location and converting it in (row, col)
            mouse_location = pygame.mouse.get_pos()
            position = (
                int(board.ROWS-(mouse_location[1]//board.square_size)),
                int((mouse_location[0]//board.square_size)+1)
            )

            if board.piece_at_case(position[0], position[1]) is not None:
                if board.piece_at_case(position[0], position[1]).color == game.turn:
                    board.update(game)
                    game.selected_piece = board.piece_at_case(position[0], position[1])
                    for move in board.piece_at_case(position[0], position[1]).moves:
                        blit_coordinate = (
                            (move[1] - 1) * board.square_size + (board.square_size / 2 - dot_size[0] / 2),
                            (((board.ROWS - move[0]) * board.square_size) + (
                                    board.square_size / 2 - dot_size[0] / 2))
                        )
                        window.blit(greendot_img, blit_coordinate)
                        pygame.display.update()
                else:
                    if game.selected_piece is not None:
                        if position in game.selected_piece.moves:
                            board.piece_at_case(position[0], position[1]).delete(board)
                            game.log_move(
                                game.selected_piece,
                                game.selected_piece.row,
                                game.selected_piece.col,
                                position[0],
                                position[1]
                            )
                            game.selected_piece.move(position[0], position[1])
                            board.update(game)
                            game.selected_piece = None
                            game.switch_turn()
                        else:
                            game.selected_piece = None
                            board.update(game)

            else:
                if game.selected_piece is not None:
                    if position in game.selected_piece.moves:
                        game.log_move(
                            game.selected_piece,
                            game.selected_piece.row,
                            game.selected_piece.col,
                            position[0],
                            position[1]
                        )
                        game.selected_piece.move(position[0], position[1])
                        board.update(game)
                        game.selected_piece = None
                        game.switch_turn()
                    else:
                        game.selected_piece = None
                        board.update(game)


'''
            if game.selected_piece is None:
                if board.piece_at_case(position[0], position[1]) is not None:
                    if board.piece_at_case(position[0], position[1]).color == game.turn:
                        game.selected_piece = board.piece_at_case(position[0], position[1])
                        for move in board.piece_at_case(position[0], position[1]).moves:
                            print(move)
                            blit_coordinate = (
                                (move[1] - 1) * board.square_size + (board.square_size / 2 - dot_size[0] / 2),
                                (((board.ROWS - move[0]) * board.square_size) + (
                                            board.square_size / 2 - dot_size[0] / 2))
                            )
                            window.blit(greendot_img, blit_coordinate)
                            pygame.display.update()
            else:
                if position in game.selected_piece.moves:
                    game.selected_piece.move(position[0], position[1])
                    print("piece moved to "+str(position[0])+str(position[1]))
                    game.selected_piece = None
                    board.update()
                    game.switch_turn()

                else:
                    game.selected_piece = None

'''
