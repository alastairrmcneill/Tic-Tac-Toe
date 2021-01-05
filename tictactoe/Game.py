import pygame
from tictactoe.Board import  Board
from tictactoe.Constants import WIN_HEIGHT, WIN_WIDTH, WHITE, BLACK, GREEN, mediumFont, largeFont, ONE_PLAYER_BUTTON, TWO_PLAYER_BUTTON

class Game:


    def __init__(self, win):
        """
        Game class that handles all the menus, player moves etc

        Arguments:
            win {pygame surface} -- Main surface to which everything gets drawn
        """
        self.win = win
        self.game_count = 0
        self.reset()
        self.computer_player = False

    def reset(self):
        """
        Resets the game class between games
        """
        self.board = Board(self.win)
        self.clock = pygame.time.Clock()
        self.game_count += 1
        if self.game_count % 2 == 0:
            self.turn = "o"
        else:
            self.turn = "x"
        self.ai = "o"
        self.player = "x"
        self.ended = False
        self.status = {}
        self.winner = ""

    def start_screen(self):
        """
        Starting menu for the game
        """
        delay = 10
        run = True

        while run:
            delay -= 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    button = self.button_from_pos(pos)
                    if button == 1:
                        print("One player")
                        self.computer_player = True
                        return
                    elif button == 2:
                        self.computer_player = False
                        return

            self.draw_start_scren()

    def draw_start_scren(self):
        """
        Drawing the starting menu
        """
        self.win.fill(WHITE)
        welcome_message = largeFont.render("Welcome to Tic Tac Toe!", False, BLACK)
        rect = welcome_message.get_rect(center=(WIN_WIDTH/2, WIN_HEIGHT/2 - 50))
        self.win.blit(welcome_message, rect)

        pygame.draw.rect(self.win, BLACK, ONE_PLAYER_BUTTON)
        onePlayer = mediumFont.render("One Player", False, WHITE)
        rect = onePlayer.get_rect(center=(150,WIN_HEIGHT - 125))
        self.win.blit(onePlayer, rect)

        pygame.draw.rect(self.win, BLACK, TWO_PLAYER_BUTTON)
        twoPlayer = mediumFont.render("Two Player", False, WHITE)
        rect = twoPlayer.get_rect(center=(450,WIN_HEIGHT - 125))
        self.win.blit(twoPlayer, rect)

        pygame.display.update()

    def end_screen(self):
        """
        End screen after the game has finished
        """
        delay = 20
        run = True
        while delay > 0:
            delay -= 1
            self.clock.tick(20)
            self.update()

        delay = 10
        while run:
            delay -= 1
            self.clock.tick(30)
            self.draw_end_scren()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONUP and delay < 0:
                    pos = pygame.mouse.get_pos()
                    button = self.button_from_pos(pos)
                    if button == 1:
                        self.reset()
                        run = False
                    elif button == 2:
                        run = False
                        pygame.quit()
                        quit()

    def draw_end_scren(self):
        """
        Draw the end screen
        """
        self.win.fill(WHITE)
        if self.status["State"] == "Won":
            end_message = largeFont.render("Winner is: " + self.status["Winner"].upper() + "!", False, BLACK)
        elif self.status["State"] == "Draw":
            end_message = largeFont.render("The game was a draw.", False, BLACK)

        rect = end_message.get_rect(center=(WIN_WIDTH/2, WIN_HEIGHT/2 - 50))
        self.win.blit(end_message, rect)

        pygame.draw.rect(self.win, BLACK, ONE_PLAYER_BUTTON)
        onePlayer = mediumFont.render("Reset", False, WHITE)
        rect = onePlayer.get_rect(center=(150,WIN_HEIGHT - 125))
        self.win.blit(onePlayer, rect)

        pygame.draw.rect(self.win, BLACK, TWO_PLAYER_BUTTON)
        twoPlayer = mediumFont.render("Quit", False, WHITE)
        rect = twoPlayer.get_rect(center=(450,WIN_HEIGHT - 125))
        self.win.blit(twoPlayer, rect)

        pygame.display.update()

    def button_from_pos(self, pos):
        """
        Determines which button is pressed depending on where is clicked on the screen. Buttons are always in the same place

        Arguments:
            pos {tuple (x, y)} -- x and y co-ordinates of the mouse click

        Returns:
            int -- number of the button clicked
        """
        if ONE_PLAYER_BUTTON[0] + ONE_PLAYER_BUTTON[2] > pos[0] > ONE_PLAYER_BUTTON[0] and ONE_PLAYER_BUTTON[1] + ONE_PLAYER_BUTTON[3] > pos[1] > ONE_PLAYER_BUTTON[1]:
            return 1

        if TWO_PLAYER_BUTTON[0] + TWO_PLAYER_BUTTON[2] > pos[0] > TWO_PLAYER_BUTTON[0] and TWO_PLAYER_BUTTON[1] + TWO_PLAYER_BUTTON[3] > pos[1] > TWO_PLAYER_BUTTON[1]:
            return 2

        return 0

    def select(self, row, col):
        """
        Checks if the square selected is empty and plays a move if it is

        Arguments:
            row {int} -- Row which was clicked
            col {int} -- Column which was clicked
        """
        if self.board.board[row][col] == 0:
            self.play(row, col)

    def play(self, row, col):
        """
        Plays a piece onto the board

        Arguments:
            row {int} -- Row to play the piece
            col {int} -- Column to play the piece
        """
        self.board.add_piece(row, col, self.turn)
        self.change_turn()

    def check_status(self):
        """
        Checks the current status and updates if the game has ended
        """
        self.status = self.board.check_status()
        if self.status["State"] != "Continue":
            self.ended = True

    def change_turn(self):
        """
        Swaps the current active player
        """
        if self.turn == "x":
            self.turn = "o"
        else:
            self.turn = "x"

    def update(self):
        """
        Draws the game to the screen
        """
        self.win.fill(WHITE)
        self.board.draw()
        pygame.display.update()