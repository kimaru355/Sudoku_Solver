#!/usr/bin/python3

import copy
from get_input import get_input
from add_sudoku import add_sudoku
from solve_sudoku import solve_sudoku
from solve_sudoku import printer

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

def start(sudoku):
    n = 1
    while True:
        printer(sudoku)
        # loop to get user input for each line
        input_list = get_input(n)
        sudoku = add_sudoku(sudoku, n - 1, input_list)
        n += 1
        if n > 9:
            break
    return sudoku

sudoku = start(sudoku)
sudoku_copy = copy.deepcopy(sudoku)
solve_sudoku(sudoku, sudoku_copy)
