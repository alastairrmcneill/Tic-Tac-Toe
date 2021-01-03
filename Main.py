"""
My python implementation of the game tic tac toe or knots and crosses or Ex's and O's
Author - Alastair McNeill
Start Date - 3rd Jan 2020
End Date - In Progress
"""

# Imports
import pygame
from tictactoe.Game import Game
from tictactoe.Constants import WIN_WIDTH, WIN_HEIGHT, SQUARE_SIZE


## Variables and constants
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
clock = pygame.time.Clock()

# Functions
def get_row_col(pos):
    row = pos[1] // SQUARE_SIZE
    col = pos[0] // SQUARE_SIZE

    return (row, col)


def main():
    run = True
    game = Game(WIN)
    game.start_screen()

    while run:
        clock.tick(30)

        if game.ended:
            game.end_screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row,col = get_row_col(pos)
                game.select(row, col)

        game.check_status()
        game.update()

    pygame.quit()
    quit()


if __name__ == '__main__':
    main()


