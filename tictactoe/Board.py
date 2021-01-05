import pygame
from tictactoe.Piece import Piece
from tictactoe.Constants import BLACK, RED, WIN_HEIGHT, WIN_WIDTH, SQUARE_SIZE

class Board:
    def __init__(self, win):
        """
        Board class holding the position of all the pieces
        Arguments:
            win {pygame surface} -- Main surface to which everything gets drawn
        """
        self.win = win
        self.board = [[0 for j in range(3)] for i in range(3)]
        self.winning_line = []

    def add_piece(self, row, col, turn):
        """
        Places a pice in the board
        Arguments:
            row {int} -- Row that the piece is placed
            col {int} -- Column that the piece is placed
            turn {string} -- is the piece an x or o
        """
        self.board[row][col] = Piece(self.win, row, col, turn)

    def get_piece(self, row, col):
        """
        Returns the piece from a given location

        Arguments:
            row {int} -- Row of piece to be returned
            col {int} -- Column of piece to be returned

        Returns:
            Piece -- Piece holding all the information of that piece
        """
        return self.board[row][col]

    def reset_piece(self, row, col):
        """
        Resets piece at location to 0

        Arguments:
            row {int} -- Row of piece to be set to 0
            col {int} -- Column of piece to be set to 0
        """
        self.board[row][col] = 0

    def get_all_pieces(self):
        """
        Returns the board in a simple format

        Returns:
            List -- 2D string list of current board state
        """

        pieces = []
        for row in self.board:
            pieces_row = []
            for elem in row:
                if elem == 0:
                    pieces_row.append(elem)
                else:
                    pieces_row.append(elem.player)
            pieces.append(pieces_row)

        return pieces



    def check_status(self):
        """
        Checks the current state of the board

        Returns:
            Dict -- Current state and if there was a winner then who it was
        """
        status = {"State": "", "Winner":""}
        pieces = self.get_all_pieces()

        # Check Rows
        for i in range(3):
            if self.equal3(pieces[i][0], pieces[i][1], pieces[i][2]):
                status = {"State": "Won", "Winner": pieces[i][0]}
                self.winning_line = [self.board[i][0], self.board[i][2]]
                return status

        # Check Cols
        for i in range(3):
            if self.equal3(pieces[0][i], pieces[1][i], pieces[2][i]):
                status = {"State": "Won", "Winner": pieces[0][i]}
                self.winning_line = [self.board[0][i], self.board[2][i]]
                return status

        # Check Diags
        if pieces[1][1] != 0:
            if self.equal3(pieces[0][0], pieces[1][1], pieces[2][2]):
                status = {"State": "Won", "Winner": pieces[1][1]}
                self.winning_line = [self.board[0][0], self.board[2][2]]
                return status

            if self.equal3(pieces[2][0], pieces[1][1], pieces[0][2]):
                status = {"State": "Won", "Winner": pieces[1][1]}
                self.winning_line = [self.board[2][0], self.board[0][2]]
                return status

        # Check full
        if self.is_full():
            status = {"State": "Draw", "Winner": ""}
            return status

        status = {"State": "Continue", "Winner": ""}
        return status




    def equal3(self, a, b, c):
        """
        Checks if three pieces are the same

        Arguments:
            a {String} -- First piece value
            b {String} -- Second piece value
            c {String} -- Third piece value

        Returns:
            Boolean -- True if they are all equal and not equal to 0
        """
        return a == b and a ==c and a != 0

    def is_full(self):
        """
        Checks if all squares have been played

        Returns:
            Boolean -- True if all squares have been played
        """
        for row in self.board:
            for elem in row:
                if elem == 0:
                    return False

        return True


    def draw(self):
        """
        Draws board, pieces and any winning marker if there is one
        """
        self.draw_board()
        self.draw_pieces()
        self.check_status()
        self.draw_winning_line()

    def draw_board(self):
        """
        Draws the board lines
        """
        for i in range(1,3):
            pygame.draw.line(self.win, BLACK, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, WIN_HEIGHT), 5)
            pygame.draw.line(self.win, BLACK, (0, i * SQUARE_SIZE), (WIN_WIDTH , i * SQUARE_SIZE), 5)

    def draw_pieces(self):
        """
        Draws the pieces on the board
        """
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                piece = self.board[i][j]
                if piece != 0:
                    piece.draw()

    def draw_winning_line(self):
        """
        Draws the winning marker if there is one
        """
        if self.winning_line != []:
            x1 = self.winning_line[0].x
            y1 = self.winning_line[0].y
            x2 = self.winning_line[1].x
            y2 = self.winning_line[1].y
            pygame.draw.line(self.win, RED, (x1, y1), (x2, y2), 10)