#!/usr/bin/python3

import copy
from print_sudoku import print_sudoku
from Runner import Runner


# run entire class and solve_sudoku
def solve_sudoku(sudoku, sudoku_copy=[]):
    runner = Runner(sudoku, sudoku_copy)
    runner.solve_sudoku_1()
    if runner.done2 is True:
        return None
    runner.sudoku_copy = copy.deepcopy(runner.sudoku)
    runner.solve_sudoku_2()


# print using print_sudoku
def printer(sudoku):
    print_sudoku(sudoku)
