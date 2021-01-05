"""
Contains the functions needed to implement minimax and minimax with alpha beta pruning
"""

def best_move(game):
    """
    Determines the best move to make from a given game state

    Arguments:
        game {Game} -- Current game state

    Returns:
        tuple -- Row and Column of best move to make
    """
    scores = {game.ai: 100, game.player: -100}

    bestScore = -1 * float("inf")

    for i in range(3):
        for j in range(3):
            if game.board.get_piece(i, j) == 0:
                game.board.add_piece(i, j, game.ai)
                score = minimax(game, scores, False)
                game.board.reset_piece(i, j)
                if score > bestScore:
                    bestScore = score
                    row = i
                    col = j
    return row, col

def minimax(game, scores, isMaximising):
    """
    Minimax algorithm to create and work through the game states in a tree form

    Arguments:
        game {Game} -- Current game state
        scores {Dict} -- Dictionary containing the scoring metrics
        isMaximising {Boolean} -- Determines if the current player is trying to maximise or minimise the score

    Returns:
        Int -- Score of the best state found
    """

    result = game.board.check_status()

    if result["State"] == "Won":
        return scores[result["Winner"]]
    elif result["State"] == "Draw":
        return 0

    if isMaximising:
        bestScore = -1 * float("inf")
        for i in range(3):
            for j in range(3):
                if game.board.get_piece(i, j) == 0:
                    game.board.add_piece(i, j, game.ai)
                    score = minimax(game, scores, False)
                    game.board.reset_piece(i, j)
                    game.board.winning_line = []
                    bestScore = max(bestScore, score)

        return bestScore

    else:
        bestScore = float("inf")
        for i in range(3):
            for j in range(3):

                if game.board.get_piece(i, j) == 0:
                    game.board.add_piece(i, j, game.player)
                    score = minimax(game, scores, True)
                    game.board.reset_piece(i, j)
                    game.board.winning_line = []
                    bestScore = min(bestScore, score)

        return bestScore

def best_move_pruning(game):
    """
    Determines the best move to make from a given game state utilising the alpha beta pruning technique
    to help speed up the algorithm

    Arguments:
        game {Game} -- Current game state

    Returns:
        Tuple -- Row and column of best move from this starting position
    """
    alpha = -1 * float("inf")
    beta = float("inf")
    scores = {game.ai: 100, game.player: -100}

    bestScore = -1 * float("inf")
    for i in range(3):
        for j in range(3):
            if game.board.get_piece(i, j) == 0:
                game.board.add_piece(i, j, game.ai)
                score = minimax_pruning(game, scores, alpha, beta, False)
                game.board.reset_piece(i, j)
                game.board.winning_line = []
                if score > bestScore:
                    bestScore = score
                    row = i
                    col = j

    return row, col

def minimax_pruning(game, scores, alpha, beta, isMaximising):
    """
    Minimax algorithm to create and work through the game states in a tree form. Implements the alpha-beta
    pruning technique to limit the number of calls to the algorithm to speed it up

    Arguments:
        game {Game} -- Current game state
        scores {Dict} -- Dictionary containing the scoring metrics
        alpha {Int} -- Current possible maximum in this branch
        beta {Int} -- Current possible minimum in this branch
        isMaximising {Boolean} -- Determines if we are maximising or minimising

    Returns:
        Int -- Score of the end state of the board
    """

    result = game.board.check_status()

    if result["State"] == "Won":
        return scores[result["Winner"]]
    elif result["State"] == "Draw":
        return 0



    if isMaximising:
        bestScore = -1 * float("inf")
        for i in range(3):
            for j in range(3):

                if game.board.get_piece(i, j) == 0:
                    game.board.add_piece(i, j, game.ai)
                    score = minimax_pruning(game, scores, alpha, beta, False)
                    game.board.reset_piece(i, j)
                    game.board.winning_line = []
                    bestScore = max(bestScore, score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break

        return bestScore


    else:
        bestScore = float("inf")
        for i in range(3):
            for j in range(3):
                if game.board.get_piece(i, j) == 0:
                    game.board.add_piece(i, j, game.player)
                    score = minimax_pruning(game, scores, alpha, beta, True)
                    game.board.reset_piece(i, j)
                    game.board.winning_line = []
                    bestScore = min(bestScore, score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break

        return bestScore



