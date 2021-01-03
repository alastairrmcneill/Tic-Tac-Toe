import pygame
from tictactoe.Constants import WHITE

class Game:
    def __init__(self, win):
        self.win = win

    def reset(self):
        pass

    def start_screen(self):
        pass

    def end_screen(self):
        pass

    def update(self):
        self.win.fill(WHITE)

        pygame.display.update()