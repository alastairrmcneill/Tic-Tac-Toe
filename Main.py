"""
My python implementation of the game tic tac toe or knots and crosses or Ex's and O's"""
import pygame
from tictactoe.Game import Game
from tictactoe.Constants import WIN_WIDTH, WIN_HEIGHT


## Variables and constants
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
clock = pygame.time.Clock()

def main():
    run = True
    game = Game(WIN)

    while run:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()
    quit()


if __name__ == '__main__':
    main()
