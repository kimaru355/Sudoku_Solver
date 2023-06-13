#!/usr/bin/python3

from get_input import get_input
from add_sudoku import add_sudoku
from solve_sudoku import solve_sudoku
from solve_sudoku import printer
from get_sudoku import get_sudoku

# sudoku format
sudoku = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]


# start - get entire sudoku form user
# @n: line to get input for and to add to sudoku
def start(sudoku):
    n = 1
    # loop to get user input for each line
    while True:
        # print sudoku for user to confirm
        printer(sudoku)
        input_list = get_input(n)
        sudoku = add_sudoku(sudoku, n - 1, input_list)
        n += 1
        if n > 9:
            break
    printer(sudoku)
    solve_sudoku(sudoku)


"""
    mul_sudoku - gets multiple sudoku puzzles and solves each of them
    @n: number of sudoku puzzles to solve
"""


def mul_sudoku(sudoku):
    n = 1
    while True:
        sudoku = get_sudoku(n)
        if sudoku is False:
            break
        n += 1
        printer(sudoku)
        solve_sudoku(sudoku)


mul_sudoku(sudoku)
start(sudoku)
