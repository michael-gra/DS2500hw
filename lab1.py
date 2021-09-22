"""
Grace Michael
DS2500: Programming with Data
Lab 1
"""

import numpy as np
import random

# X = 1
# O = 0
# empty = 2

# variables used in array
nums = [0, 1, 2]

# practice board
board1 = np.array([[1, 1, 2],
                  [0, 2, 1],
                  [2, 0, 1]])

# function analyzes winner of inputted board
def winner(board):
    # horizontals
    if board[0][0] == board[0][1] and board[0][0] == board[0][2]:
        winner = board[0][0]
        if winner == 1:
            return 'Winner is X!'
        if winner == 0:
            return 'Winner is O!'
        if winner == 2:
            return 'The game is a draw.'
    if board[1][0] == board[1][1] and board[1][0] == board[1][2]:
        winner = board[1][0]
        if winner == 1:
            return 'Winner is X!'
        if winner == 0:
            return 'Winner is O!'
        if winner == 2:
            return 'The game is a draw.'
    if board[2][0] == board[2][1] and board[2][0] == board[2][2]:
        winner = board[2][0]
        if winner == 1:
            return 'Winner is X!'
        if winner == 0:
            return 'Winner is O!'
        if winner == 2:
            return 'The game is a draw.'
    # verticals
    if board[0][0] == board[1][0] and board[0][0] == board[2][0]:
        winner = board[0][0]
        if winner == 1:
            return 'Winner is X!'
        if winner == 0:
            return 'Winner is O!'
        if winner == 2:
            return 'The game is a draw.'
    if board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        winner = board[0][1]
        if winner == 1:
            return 'Winner is X!'
        if winner == 0:
            return 'Winner is O!'
        if winner == 2:
            return 'The game is a draw.'
    if board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        winner = board[0][2]
        if winner == 1:
            return 'Winner is X!'
        if winner == 0:
            return 'Winner is O!'
        if winner == 2:
            return 'The game is a draw.'
    # diagnols
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        winner = board[0][0]
        if winner == 1:
            return 'Winner is X!'
        if winner == 0:
            return 'Winner is O!'
        if winner == 2:
            return 'The game is a draw.'
    if board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        winner = board[0][2]
        if winner == 1:
            return 'Winner is X!'
        if winner == 0:
            return 'Winner is O!'
        if winner == 2:
            return 'The game is a draw.'
    else:
        return 'The game is a draw.'
    return winner

def main():
    # game board is randomized
    board = np.random.choice(nums, size=(3,3))
    print(board)
    print(winner(board))


if __name__ == '__main__':
    main()
