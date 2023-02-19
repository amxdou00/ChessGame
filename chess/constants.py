import pygame
import os

# Constants
WINDOW_SIZE = 800
FPS = 60
sides = ["black","white"]
piece_size = (80, 80)
dot_size = (30,30)
pieces_img_path = "images/pieces"
other_img_path = "images"


# Importing the images
wking_img = pygame.transform.scale(pygame.image.load(os.path.join(pieces_img_path, 'wking.png')), piece_size)
wqueen_img = pygame.transform.scale(pygame.image.load(os.path.join(pieces_img_path, 'wqueen.png')), piece_size)
wrook_img = pygame.transform.scale(pygame.image.load(os.path.join(pieces_img_path, 'wrook.png')), piece_size)
wbishop_img = pygame.transform.scale(pygame.image.load(os.path.join(pieces_img_path, 'wbishop.png')), piece_size)
wpawn_img = pygame.transform.scale(pygame.image.load(os.path.join(pieces_img_path, 'wpawn.png')), piece_size)
wknight_img = pygame.transform.scale(pygame.image.load(os.path.join(pieces_img_path, 'wknight.png')), piece_size)
bking_img = pygame.transform.scale(pygame.image.load(os.path.join(pieces_img_path, 'bking.png')), piece_size)
bqueen_img = pygame.transform.scale(pygame.image.load(os.path.join(pieces_img_path, 'bqueen.png')), piece_size)
brook_img = pygame.transform.scale(pygame.image.load(os.path.join(pieces_img_path, 'brook.png')), piece_size)
bbishop_img = pygame.transform.scale(pygame.image.load(os.path.join(pieces_img_path, 'bbishop.png')), piece_size)
bpawn_img = pygame.transform.scale(pygame.image.load(os.path.join(pieces_img_path, 'bpawn.png')), piece_size)
bknight_img = pygame.transform.scale(pygame.image.load(os.path.join(pieces_img_path, 'bknight.png')), piece_size)

game_icon = pygame.image.load(os.path.join(other_img_path,"game_icon.png"))
greendot_img = pygame.transform.scale(pygame.image.load(os.path.join(other_img_path,"Basic_green_dot.png")), dot_size)
greencross_img = pygame.transform.scale(pygame.image.load(os.path.join(other_img_path,"green_cross.png")), dot_size)

