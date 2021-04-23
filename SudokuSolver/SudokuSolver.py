import pprint
import time
import numpy as np
from numpy import random

start_time = time.time()


def generate(board):

        for row in range(0, len(board[0])):
                for col in range(0, len(board[0])):
                        bool = False
                        while bool is False:
                                num = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
                                board[row][col] = num
                                if (checker(board, row, col, num)):
                                        bool = True
        return None


def solve(board):
#Uses backtracking algorithm to solve sudoku board
#
        find = find_empty(board)
        if find:
                (row,col) = find
        else:
                return True

        for num in range (1, 10):
                if checker(board, row, col, num):
                        board[row][col] = num

                        if solve(board):
                                return True

                        board[row][col] = 0
        return False

def checker(board, row, col, num):
#Validates the number inputed into a specific cell
#in the Sudoku board by checking the horizontal, vertical,
#and box constraints of the Sudoku game
#CHECK ROW
        for i in range(0, len(board[0])):
                if board[row][i] == num and col != i:
                        return False

#CHECK COLUMN
        for i in range(0, len(board[0])):
                if board[i][col] == num and row != i:
                        return False

#CHECK BOX
        perx = row // 3 * 3
        pery = col // 3 * 3

        for i in range(perx, perx+3):
                for j in range(pery, pery+3):
                        if board[i][j] == num and row != i and col != j:
                                return False

        return True

def find_empty(board):
#Finds an empty spot on the sudoku board (represented by 0)
#and returns the position (row#,col#) to solve function
        for i in range (len(board)):
                for j in range (len(board[0])):
                        if board[i][j] == 0:
                                return (i, j)
        return None

BOARD = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

'''
BOARD = np.zeros((9,9))
generate(BOARD)
print(BOARD)
'''


pp = pprint.PrettyPrinter(width=41, compact=True)
solve(BOARD)
pp.pprint(BOARD)

print("--- %s seconds ---" % (time.time() - start_time))
