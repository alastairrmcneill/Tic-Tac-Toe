import pygame
from tictactoe.Constants import SQUARE_SIZE, pieceFont, BLACK

class Piece:
    def __init__(self, win, row, col, player):
        self.win = win
        self.row = row
        self.col = col
        self.player = player
        self.x = 0
        self.y = 0
        self.get_pos()

    def get_pos(self):
        self.x = self.col * SQUARE_SIZE + SQUARE_SIZE // 2
        self.y = self.row * SQUARE_SIZE + SQUARE_SIZE // 2

    def draw(self):
        text = pieceFont.render(self.player, False, BLACK)
        rect = text.get_rect(center= (self.x, self.y))

        self.win.blit(text, rect)
