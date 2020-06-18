"""
Tic Tac Toe Player
"""

import math
import copy

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
    if board == initial_state():
        return X
    
    num_X, num_O = 0, 0
    for row in board:
        num_X += row.count(X)
        num_O += row.count(O)
    
    if num_X == num_O:
        return X
    
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                possible_actions.append([i, j])
    
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    curr_player = player(board)
    try:
        if new_board[action[0]][action[1]] != EMPTY:
            raise IndexError
        else:
            new_board[action[0]][action[1]] = curr_player
            return new_board
    
    except IndexError:
        print('Spot already occupied')


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check rows
    for row in board:
        num_x = row.count(X)
        num_o = row.count(O)
        if num_x == 3:
            return X
        
        if num_o == 3:
            return O
    
    # check for columns
    for i in range(len(board)):
        column = [row[i] for row in board]
        num_o = column.count(O)
        num_x = column.count(X)
        if num_x == 3:
            return X
        if num_o == 3:
            return O
    
    #check for diagonals
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    
    if board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    
    if board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return X

    if board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O
    
    return None
 

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    empty_count = 0
    for row in board:
        empty_count += row.count(EMPTY)
    
    if empty_count == 0:
        return True

    elif winner(board) is not None:
        return True
    
    else:
        return False
    

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    
    elif winner(board) == O:
        return -1
    
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    curr_player = player(board)
    alpha, beta = -math.inf, math.inf
    if curr_player == X:
        v = -math.inf
        for action in actions(board):
            k = Min_val(result(board, action), alpha, beta)
            if k > v:
                v = k
                best_action = action
        
    else:
        v = math.inf
        for action in actions(board):
            k = Max_val(result(board, action), alpha, beta)
            if k < v:
                v = k
                best_action = action

    return best_action


def Max_val(board, alpha, beta):
    if terminal(board):
        return utility(board)
    
    v = -math.inf
    for action in actions(board):
        v = max(v, Min_val(result(board, action), alpha, beta))
        if v >= beta:
            return v
        alpha = max(v, alpha)
    return v

def Min_val(board, alpha, beta):
    if terminal(board):
        return utility(board)
    
    v = math.inf
    for action in actions(board):
        v = min(v, Max_val(result(board, action), alpha, beta))
        if v <= alpha:
            return v
        beta = min(v, beta)
    return v