#!/usr/bin/python3

from SolveSudoku import SolveSudoku
# Irregular - check sudoku for irregularities


class Irregular(SolveSudoku):
    def check_irregular(self):
        # check if any value appears more than once in square
        # horizontal and vertical
        for j in range(1, 10):
            # check squares
            if self.square_1.count(j) > 1:
                return True
            if self.square_2.count(j) > 1:
                return True
            if self.square_3.count(j) > 1:
                return True
            if self.square_4.count(j) > 1:
                return True
            if self.square_5.count(j) > 1:
                return True
            if self.square_6.count(j) > 1:
                return True
            if self.square_7.count(j) > 1:
                return True
            if self.square_8.count(j) > 1:
                return True
            if self.square_9.count(j) > 1:
                return True
            # check vertical
            if self.vertical_1.count(j) > 1:
                return True
            if self.vertical_2.count(j) > 1:
                return True
            if self.vertical_3.count(j) > 1:
                return True
            if self.vertical_4.count(j) > 1:
                return True
            if self.vertical_5.count(j) > 1:
                return True
            if self.vertical_6.count(j) > 1:
                return True
            if self.vertical_7.count(j) > 1:
                return True
            if self.vertical_8.count(j) > 1:
                return True
            if self.vertical_9.count(j) > 1:
                return True
        # check horizontal
        for i in range(9):
            for j in range(1, 10):
                if self.sudoku[i].count(j) > 1:
                    return True
        return False
