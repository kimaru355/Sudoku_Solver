#!/usr/bin/python3

from get_input import get_input
from add_sudoku import add_sudoku
from solve_sudoku import solve_sudoku
from get_test import get_sudoku
from get_test import send_sudoku
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

# start - sudoku solver starts here


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
    send_sudoku(sudoku)


start(sudoku)
sudoku = get_sudoku()
sudoku_copy = get_sudoku()

solve_sudoku(sudoku, sudoku_copy)
