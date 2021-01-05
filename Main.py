"""
My python implementation of the game tic tac toe or knots and crosses or Ex's and O's
Author - Alastair McNeill
Start Date - 3rd Jan 2021
End Date - 5th Jan 2021
"""

# Imports
import pygame
from tictactoe.Game import Game
from tictactoe.Constants import WIN_WIDTH, WIN_HEIGHT, SQUARE_SIZE
from minimax.minimax import best_move_pruning


## Variables and constants
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
clock = pygame.time.Clock()

# Functions
def get_row_col(pos):
    """
    Function takes a mouse click position and returnts the corresponding row and column in the game
    Arguments:
        pos {tuple (x, y)} -- x and y co-ordinates

    Returns:
        tuple (row, col) -- row and column in game where the click happened
    """
    row = pos[1] // SQUARE_SIZE
    col = pos[0] // SQUARE_SIZE

    return (row, col)


def main():
    """
    Main game loop, inlcudes start screen, end screen, ai player and munual player
    """
    run = True
    game = Game(WIN)
    game.start_screen()

    while run:
        clock.tick(30)

        game.check_status()

        if game.computer_player and game.turn == game.ai and not game.ended:
            row, col = best_move_pruning(game)
            game.play(row, col)

        if game.ended:
            game.end_screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row,col = get_row_col(pos)
                game.select(row, col)

        game.update()

    pygame.quit()
    quit()


if __name__ == '__main__':
    main()


