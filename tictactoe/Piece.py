import pygame
from tictactoe.Constants import SQUARE_SIZE, pieceFont, BLACK

class Piece:
    def __init__(self, win, row, col, player):
        """
        Piece class which holds the information on the players moves

        Arguments:
            win {pygame surface} -- Main surface to which everything gets drawn
            row {int} -- row in the board to place the piece
            col {int} -- column in the board to place the piece
            player {string} -- is the player an x or an o
        """
        self.win = win
        self.row = row
        self.col = col
        self.player = player
        self.x = 0
        self.y = 0
        self.get_pos()

    def get_pos(self):
        """
        Finds the x and y co-ordinates of the center of the piece
        """
        self.x = self.col * SQUARE_SIZE + SQUARE_SIZE // 2
        self.y = self.row * SQUARE_SIZE + SQUARE_SIZE // 2

    def draw(self):
        """
        Draws piece to the window
        """
        text = pieceFont.render(self.player, False, BLACK)
        rect = text.get_rect(center= (self.x, self.y))

        self.win.blit(text, rect)
