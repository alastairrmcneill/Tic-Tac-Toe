"""
Constants for the game
"""

import pygame
pygame.font.init()

# Window variables
WIN_WIDTH = 600
WIN_HEIGHT = 600
SQUARE_SIZE = WIN_WIDTH // 3

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 210, 0)
RED = (255, 0, 0)

# Fonts
largeFont = pygame.font.SysFont("Marker Felt", 50)
mediumFont = pygame.font.SysFont("Marker Felt", 30)
pieceFont = pygame.font.SysFont(("Marker Felt"), 250)

# Buttons
ONE_PLAYER_BUTTON = (75, 450, 150, 50)
TWO_PLAYER_BUTTON = (375, 450, 150, 50)



