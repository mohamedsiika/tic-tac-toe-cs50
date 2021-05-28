"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None
answer=(0,0)


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
    if board==initial_state():
        return X
    if sum(row.count(X) for row in board) > sum(row.count(O) for row in board):
        return O
    else:
        return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves=[]
    for i in range(3):
        for j in range (3):
            if board[i][j] == EMPTY:
                moves.append((i,j))
    return moves


def result(board, action):
    """
    Returns the board that results  from making move (i, j) on the board.
    """

    copyy = copy.deepcopy(board)
    if player(board)==X:
        copyy[action[0]][action[1]]=X
    else:
        copyy[action[0]][action[1]]=O
    return copyy




def winner(board):
    if (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X') or \
            (board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X') or \
            (board[0] == ['X', 'X', 'X'] or board[1] == ['X', 'X', 'X'] or board[2] == ['X', 'X', 'X']) or \
            (board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X') or \
            (board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X') or \
            (board[2][2] == 'X' and board[0][2] == 'X' and board[1][2] == 'X'):
        return X

    elif (board[0][0]=='O' and board[1][1]=='O' and board[2][2]=='O') or\
            (board[0][2]=='O' and board[1][1]=='O' and board[2][0]=='O') or\
            (board[0]==['O','O','O'] or board[1]==['O','O','O'] or board[2]==['O','O','O']) or\
            (board[0][0]=='O' and board[1][0]=='O' and board[2][0]=='O') or\
            (board[0][1]=='O' and board[1][1]=='O' and board[2][1]=='O') or\
            (board[2][2]=='O' and board[0][2]=='O' and board[1][2]=='O'):
        return O
    else:
        return None
        raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board)==X or winner(board)==O:
        return True
    elif sum(row.count(EMPTY) for row in board)==0:
        return True
    else:
       return False



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X  :
        return 1
    elif winner(board)==O:
        return -1
    else:
       return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(board):
           if terminal(board):
               return utility(board)
           v=-100000000
           for action in actions(board):
              v=max(v,min_value(result(board,action)))


           return v

    def min_value(board):
        if terminal(board):
            return utility(board)
        v = 100000000
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
        return v

    if player(board)==X:
        v = -math.inf
        for action in actions(board):
            k = min_value(result(board, action))
            if k > v:
                v = k
                best_move = action
    else:
        v = math.inf
        for action in actions(board):
            k = max_value(result(board, action))  # FIXED
            if k < v:
                v = k
                best_move = action
    return best_move
