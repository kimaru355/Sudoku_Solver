#!/usr/bin/python3

# add_sudoku - adds user input to sudoku
# @n: line to add input
# @input_list: list containing digits to add to line(n) of sudoku


def add_sudoku(sudoku, n, input_list):
    # loop to add user input to sudoku
    for i in range(len(sudoku[n])):
        sudoku[n][i] = input_list[i]

    # return modified sudoku
    return sudoku
