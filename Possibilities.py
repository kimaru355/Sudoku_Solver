#!/usr/bin/python3

from Sudoku import Sudoku

"""
    Possibilities - checks all possibilities in sudoku
    @Sudoku: parent class of Possibilities
"""


class Possibilities(Sudoku):
    # check all possibilities in the sudoku
    def check_possibilities(self):
        self.possible = []
        # create empty 2D list to store lists and form 3D list
        for i in range(9):
            ind = []
            self.possible.append(ind)

        for i in range(9):
            for j in range(9):
                test = []
                # add value if not 0 which indicates empty
                if self.sudoku[i][j] != 0:
                    test.append(self.sudoku[i][j])
                    self.possible[i].append(test)
                    continue
                for k in range(1, 10):
                    # check squares
                    if i < 3 and j < 3 and k not in self.square_1:
                        test.append(k)
                    elif i < 3 and 2 < j < 6 and k not in self.square_2:
                        test.append(k)
                    elif i < 3 and 5 < j < 9 and k not in self.square_3:
                        test.append(k)
                    elif 2 < i < 6 and j < 3 and k not in self.square_4:
                        test.append(k)
                    elif 2 < i < 6 and 2 < j < 6 and k not in self.square_5:
                        test.append(k)
                    elif 2 < i < 6 and 5 < j < 9 and k not in self.square_6:
                        test.append(k)
                    elif 5 < i < 9 and j < 3 and k not in self.square_7:
                        test.append(k)
                    elif 5 < i < 9 and 2 < j < 6 and k not in self.square_8:
                        test.append(k)
                    elif 5 < i < 9 and 5 < j < 9 and k not in self.square_9:
                        test.append(k)
                    # check horizontal lines
                    if k not in self.sudoku[i]:
                        test.append(k)
                    # check vertical lines
                    if j == 0 and k not in self.vertical_1:
                        test.append(k)
                    elif j == 1 and k not in self.vertical_2:
                        test.append(k)
                    elif j == 2 and k not in self.vertical_3:
                        test.append(k)
                    elif j == 3 and k not in self.vertical_4:
                        test.append(k)
                    elif j == 4 and k not in self.vertical_5:
                        test.append(k)
                    elif j == 5 and k not in self.vertical_6:
                        test.append(k)
                    elif j == 6 and k not in self.vertical_7:
                        test.append(k)
                    elif j == 7 and k not in self.vertical_8:
                        test.append(k)
                    elif j == 8 and k not in self.vertical_9:
                        test.append(k)

                # append all possibilities that are not in vertical,
                # square and horizontal
                tested = []
                for k in range(1, 10):
                    if test.count(k) == 3:
                        tested.append(k)
                self.possible[i].append(tested)
