#!/usr/bin/python3

from Possibilities import Possibilities

# SolveSudoku - child class of Possibilities and solves by
# adding possible to sudoku


class SolveSudoku(Possibilities):
    def solve_puzzle(self):
        m = n = 0
        for i in range(9):
            for j in range(9):
                # add if len of possible values is 1 and
                # value to be replaced is 0
                if len(self.possible[i][j]) == 1 and self.sudoku[i][j] == 0:
                    n += 1
                    self.sudoku[i][j] = self.possible[i][j][0]
        if m == n:
            # check if done solving possible
            self.done1 = True
