import pygame

class Piece:
    def __init__(self, win, row, col, player):
        self.win = win
        self.row = row
        self.col = col
        self.player = player

    def draw(self):
        pass