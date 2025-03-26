"""
Tic Tac Toe Player
"""
import random
import logging
logging.basicConfig(level=logging.DEBUG)
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    
    """
    Returns player who has the next turn on a board.
    """
    X_count = sum(row.count(X) for row in board)
    O_count = sum(row.count(O) for row in board)

    return X if X_count == O_count else O

    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    board = [[None if cell == "" or cell == " " else cell for cell in row] for row in board]
    
    possible_moves = set()

    for i in range(3): 
        for j in range(3):  
            if board[i][j] is EMPTY:  
                possible_moves.add((i, j)) 
    logging.debug(f"Possible moves: {possible_moves}")
    return possible_moves


def result(board, action):
    """
    Returns a new board state after applying the given action.
    The original board remains unchanged.
    """
    i, j = action

    # board = [[None if cell == "" or cell == " " else cell for cell in row] for row in board]

    if not (0 <= i <= 2 and 0 <= j <=2):
        raise ValueError("Invalid move: Out of bounds.")


    if board[i][j] is not EMPTY:  
        raise ValueError("Invalid move: Cell is already occupied.")

    new_board = [row[:] for row in board]  
    new_board[i][j] = player(board) 

    return new_board  

def winner(board):
    """
    Returns the winner of the game if there is one.
    """

    board = [[None if cell == "" or cell == " " else cell for cell in row] for row in board]

    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not EMPTY:
            return row[0]
    for col in range(3):

        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not EMPTY:
            return board[0][col] 
        
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2] 
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    for row in board:
        if EMPTY in row:
            return False

    return True

def utility(board):
    """
    Returns the utility of the board:
    1 if X wins, -1 if O wins, 0 if tie.
    """
    winner_player = winner(board)
    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    else:
        return 0


def minimax(board):
    if terminal(board):
        return EMPTY
    
    current_player = player(board)
    best_value = float('-inf')
    best_moves = []

    for action in actions(board):
        new_board = result(board, action)
        value = minimax_value(new_board)
            
    if (current_player == X and value > best_value) or (current_player == 0 and value < best_value):
        best_value = value
        best_moves = [action]
    elif value == best_value:
        best_moves.append(action)

    return random.choice(best_moves)


def minimax_value(board):
    if terminal(board):
        return utility(board)
    
    if player(board) == X:
        value = float('-inf')
        for action in actions(board):
            new_value = minimax_value(result(board, action))
            print(f"Evaluating X action {action}, value = {new_value}")
            value = max(value, new_value)
        return value
    else:
        value = float('inf')
        for action in actions(board):
            new_value = minimax_value(result(board, action))
            print(f"Evaluating O action {action}, value = {new_value}")
            value = min(value, new_value)
        return value

    raise NotImplementedError
