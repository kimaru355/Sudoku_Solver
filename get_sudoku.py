#!/usr/bin/python3

"""
    get_sudoku - get sudoku as is. Used for testing multiple at once
    @n: nth sudoku to retrieve
"""


def get_sudoku(n):
    if n == 1:
        sudoku = [[0, 7, 0, 0, 0, 1, 0, 0, 0],
                  [0, 0, 0, 9, 0, 0, 0, 7, 6],
                  [6, 0, 3, 0, 0, 0, 9, 5, 0],
                  [0, 0, 0, 6, 0, 0, 5, 0, 0],
                  [0, 6, 2, 3, 0, 8, 0, 0, 0],
                  [7, 0, 1, 0, 0, 9, 0, 0, 8],
                  [1, 3, 4, 8, 9, 0, 0, 6, 2],
                  [0, 9, 6, 4, 7, 0, 1, 8, 5],
                  [0, 0, 0, 1, 2, 0, 3, 0, 0]]
        return sudoku
    elif n == 2:
        sudoku = [[0, 0, 0, 6, 0, 0, 1, 0, 7],
                  [6, 8, 0, 9, 5, 1, 3, 0, 0],
                  [0, 0, 3, 0, 0, 2, 5, 6, 8],
                  [0, 4, 0, 8, 1, 0, 0, 2, 0],
                  [0, 0, 0, 0, 0, 0, 8, 5, 0],
                  [0, 9, 0, 0, 6, 5, 0, 7, 3],
                  [4, 0, 9, 0, 0, 3, 0, 8, 5],
                  [1, 6, 2, 0, 0, 9, 0, 3, 0],
                  [5, 0, 0, 7, 0, 6, 0, 0, 0]]
        return sudoku
    elif n == 3:
        sudoku = [[0, 0, 0, 9, 8, 4, 0, 0, 0],
                  [4, 6, 0, 0, 0, 0, 8, 0, 0],
                  [2, 0, 0, 6, 0, 3, 0, 4, 0],
                  [0, 2, 0, 0, 0, 0, 0, 0, 6],
                  [9, 0, 0, 0, 0, 2, 0, 5, 0],
                  [0, 7, 0, 0, 9, 0, 0, 8, 0],
                  [0, 0, 2, 0, 7, 8, 4, 1, 5],
                  [8, 1, 0, 0, 2, 0, 0, 6, 0],
                  [0, 3, 0, 5, 0, 0, 0, 0, 0]]
        return sudoku
    elif n == 4:
        sudoku = [[4, 0, 0, 0, 0, 0, 0, 0, 7],
                  [0, 0, 2, 0, 8, 0, 5, 3, 0],
                  [0, 0, 0, 7, 5, 0, 0, 0, 9],
                  [0, 0, 5, 8, 7, 0, 0, 6, 2],
                  [6, 0, 3, 9, 2, 0, 0, 8, 0],
                  [0, 9, 0, 0, 6, 5, 0, 0, 0],
                  [0, 0, 7, 0, 0, 0, 0, 0, 0],
                  [0, 0, 6, 0, 0, 7, 2, 0, 0],
                  [0, 0, 0, 0, 9, 1, 7, 0, 3]]
        return sudoku
    elif n == 5:
        sudoku = [[0, 0, 0, 0, 6, 5, 9, 2, 8],
                  [1, 0, 5, 0, 2, 0, 7, 6, 0],
                  [0, 0, 2, 8, 0, 0, 0, 0, 0],
                  [5, 3, 0, 4, 8, 9, 0, 0, 0],
                  [6, 4, 0, 7, 0, 0, 8, 3, 0],
                  [0, 0, 7, 0, 1, 0, 0, 4, 9],
                  [4, 9, 0, 0, 0, 8, 1, 5, 7],
                  [0, 1, 8, 0, 0, 0, 3, 0, 0],
                  [0, 0, 0, 0, 9, 1, 2, 0, 0]]
        return sudoku
    elif n == 6:
        sudoku = [[0, 0, 0, 0, 6, 0, 5, 0, 0],
                  [2, 0, 0, 0, 0, 3, 0, 0, 0],
                  [0, 0, 3, 9, 0, 4, 8, 0, 0],
                  [0, 4, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 2, 0, 0, 0, 0],
                  [0, 3, 2, 7, 1, 5, 4, 0, 6],
                  [0, 7, 8, 5, 4, 1, 9, 0, 0],
                  [4, 0, 0, 0, 7, 0, 0, 8, 0],
                  [0, 6, 1, 0, 9, 0, 3, 0, 0]]
        return sudoku
    elif n == 7:
        sudoku = [[0, 0, 0, 0, 0, 6, 3, 0, 0],
                  [0, 6, 8, 0, 0, 7, 0, 0, 2],
                  [0, 1, 0, 0, 0, 8, 5, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 8, 0, 0, 5, 0, 2, 0, 0],
                  [0, 4, 0, 0, 0, 1, 0, 7, 0],
                  [4, 0, 0, 0, 1, 0, 0, 0, 3],
                  [6, 0, 3, 0, 0, 0, 0, 0, 0],
                  [0, 2, 0, 0, 9, 0, 4, 0, 0]]
        return sudoku
    elif n == 8:
        sudoku = [[0, 0, 4, 9, 0, 3, 0, 0, 0],
                  [0, 9, 0, 5, 0, 0, 0, 0, 7],
                  [0, 3, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 9, 3, 5],
                  [4, 1, 0, 0, 0, 0, 7, 0, 0],
                  [8, 0, 0, 0, 0, 0, 4, 0, 0],
                  [0, 0, 0, 0, 0, 4, 0, 0, 2],
                  [0, 0, 0, 0, 7, 0, 0, 5, 0],
                  [6, 0, 2, 0, 1, 0, 0, 0, 0]]
        return sudoku
    elif n == 9:
        sudoku = [[0, 0, 9, 0, 0, 5, 2, 0, 0],
                  [3, 5, 0, 0, 6, 0, 1, 0, 0],
                  [0, 0, 7, 0, 0, 0, 0, 3, 0],
                  [0, 9, 0, 0, 0, 0, 0, 0, 0],
                  [5, 1, 0, 0, 0, 2, 0, 8, 0],
                  [0, 0, 0, 0, 7, 0, 0, 0, 2],
                  [0, 0, 3, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 4, 0, 0, 6, 0, 0],
                  [8, 2, 0, 0, 0, 7, 0, 1, 0]]
        return sudoku
    elif n == 9:
        sudoku = [[3, 4, 0, 0, 5, 0, 0, 0, 0],
                  [0, 7, 1, 0, 2, 9, 0, 0, 5],
                  [2, 5, 0, 0, 0, 0, 9, 8, 0],
                  [7, 6, 0, 9, 0, 0, 0, 0, 8],
                  [5, 0, 0, 4, 0, 7, 0, 0, 2],
                  [0, 3, 0, 0, 0, 6, 0, 4, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 0, 4, 3, 0, 6, 0],
                  [0, 0, 0, 0, 0, 0, 5, 2, 4]]
        return sudoku
    elif n == 10:
        sudoku = [[0, 9, 0, 6, 5, 0, 0, 0, 0],
                  [0, 0, 0, 0, 9, 2, 6, 0, 1],
                  [7, 6, 0, 0, 0, 0, 2, 9, 0],
                  [4, 0, 8, 0, 0, 5, 0, 0, 0],
                  [0, 0, 0, 2, 7, 9, 4, 5, 8],
                  [0, 0, 0, 0, 0, 4, 0, 0, 0],
                  [0, 4, 0, 0, 0, 0, 1, 0, 0],
                  [0, 8, 0, 9, 0, 6, 0, 3, 4],
                  [5, 0, 0, 0, 4, 0, 9, 0, 7]]
        return sudoku
    elif n == 11:
        sudoku = [[4, 3, 5, 0, 0, 0, 6, 9, 0],
                  [0, 7, 0, 3, 0, 9, 1, 0, 5],
                  [0, 0, 1, 0, 5, 0, 3, 0, 7],
                  [0, 0, 3, 4, 2, 0, 8, 0, 0],
                  [8, 6, 0, 9, 0, 0, 0, 0, 4],
                  [5, 0, 4, 0, 0, 3, 0, 1, 0],
                  [7, 4, 0, 1, 3, 0, 0, 0, 0],
                  [6, 1, 0, 5, 9, 0, 0, 0, 0],
                  [0, 0, 8, 0, 6, 4, 0, 0, 1]]
        return sudoku
    elif n == 12:
        sudoku = [[0, 0, 2, 0, 0, 1, 0, 4, 8],
                  [0, 0, 0, 2, 0, 0, 0, 9, 0],
                  [4, 7, 0, 3, 0, 0, 6, 0, 2],
                  [0, 1, 0, 0, 3, 2, 0, 0, 0],
                  [0, 2, 0, 0, 0, 0, 0, 0, 0],
                  [0, 4, 8, 0, 0, 0, 1, 2, 3],
                  [0, 0, 0, 7, 0, 8, 4, 5, 0],
                  [0, 5, 4, 0, 0, 0, 0, 7, 9],
                  [7, 0, 1, 4, 0, 0, 0, 0, 0]]
        return sudoku
    else:
        return False
