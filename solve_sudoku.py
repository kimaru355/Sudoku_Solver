#!/usr/bin/python3

from print_sudoku import print_sudoku

# Sudoku - parent of all classes


class Sudoku:
    # define all attributes
    def __init__(self, sudoku, sudoku_copy):
        self.sudoku = sudoku
        self.sudoku_copy = sudoku_copy
        self.square_1 = []
        self.square_2 = []
        self.square_3 = []
        self.square_4 = []
        self.square_5 = []
        self.square_6 = []
        self.square_7 = []
        self.square_8 = []
        self.square_9 = []
        self.vertical_1 = []
        self.vertical_2 = []
        self.vertical_3 = []
        self.vertical_4 = []
        self.vertical_5 = []
        self.vertical_6 = []
        self.vertical_7 = []
        self.vertical_8 = []
        self.vertical_9 = []
        self.possible = []
        self.done1 = False
        self.sorted = {}

    def sudoku_parts(self):
        # split sudoku into vertical and 3x3 square parts
        self.square_1 = []
        self.square_2 = []
        self.square_3 = []
        self.square_4 = []
        self.square_5 = []
        self.square_6 = []
        self.square_7 = []
        self.square_8 = []
        self.square_9 = []
        self.vertical_1 = []
        self.vertical_2 = []
        self.vertical_3 = []
        self.vertical_4 = []
        self.vertical_5 = []
        self.vertical_6 = []
        self.vertical_7 = []
        self.vertical_8 = []
        self.vertical_9 = []
        for i in range(3):
            for j in range(3):
                self.square_1.append(self.sudoku[i][j])
        for i in range(3):
            for j in range(3, 6):
                self.square_2.append(self.sudoku[i][j])
        for i in range(3):
            for j in range(6, 9):
                self.square_3.append(self.sudoku[i][j])
        for i in range(3, 6):
            for j in range(3):
                self.square_4.append(self.sudoku[i][j])
        for i in range(3, 6):
            for j in range(3, 6):
                self.square_5.append(self.sudoku[i][j])
        for i in range(3, 6):
            for j in range(6, 9):
                self.square_6.append(self.sudoku[i][j])
        for i in range(6, 9):
            for j in range(3):
                self.square_7.append(self.sudoku[i][j])
        for i in range(6, 9):
            for j in range(3, 6):
                self.square_8.append(self.sudoku[i][j])
        for i in range(6, 9):
            for j in range(6, 9):
                self.square_9.append(self.sudoku[i][j])
        for i in range(9):
            self.vertical_1.append(self.sudoku[i][0])
        for i in range(9):
            self.vertical_2.append(self.sudoku[i][1])
        for i in range(9):
            self.vertical_3.append(self.sudoku[i][2])
        for i in range(9):
            self.vertical_4.append(self.sudoku[i][3])
        for i in range(9):
            self.vertical_5.append(self.sudoku[i][4])
        for i in range(9):
            self.vertical_6.append(self.sudoku[i][5])
        for i in range(9):
            self.vertical_7.append(self.sudoku[i][6])
        for i in range(9):
            self.vertical_8.append(self.sudoku[i][7])
        for i in range(9):
            self.vertical_9.append(self.sudoku[i][8])


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

# run entire class


class Runner(Irregular):
    # solve sudoku where one possible value exists


    def solve_sudoku_1(self):
        self.done1 = False
        # solve until no changes are made and done1 is true
        while self.done1 is False:
            self.sudoku_parts()
            self.check_possibilities()
            self.solve_puzzle()
        status = self.check_irregular()
        # check if sudoku is busted(a number is repeating)
        if status is True:
            return False
        else:
            return True

    # check sudoku where only two possible values exist


    def sort_sudoku(self):
        self.sudoku_parts()
        self.check_possibilities()
        self.sorted = {}

        # add the two possibilities and their location to a dict sorted
        for i in range(9):
            for j in range(9):
                if len(self.possible[i][j]) == 2:
                    self.sorted[f"{i}{j}"] = self.possible[i][j]

    # restores sudoku

    def restore_sudoku(self):
        for i in range(9):
            for j in range(9):
                self.sudoku[i][j] = self.sudoku_copy[i][j]

    #check if sudoku is complete

    def check_complete(self):
        for i in range(9):
            for j in range(9):
                if self.sudoku[i][j] == 0:
                    return False
        print_sudoku(self.sudoku)
    # test each option


    def tester(self, lst):
        a = 0
        self.restore_sudoku()
        for k in self.sorted:
            self.sudoku[int(k[0])][int(k[1])] = self.sorted[k][lst[a]]
            a += 1
            if a == len(lst) - 1:
                break
        self.sudoku_parts()
        self.check_possibilities()
        status = self.check_irregular()
        if status is True:
            pass
        else:
            status = self.solve_sudoku_1()
            if status is True:
                print_sudoku(self.sudoku)
                self.check_complete()

        # use recursion to create possible outcomes


    def rec(self, lst, m, n, f):
        for i in range(2):
            lst.append(i)
            if n != 0:
                self.rec(lst, m, n - 1, f + 1)
            if m == f:
                self.tester(lst)
            while len(lst) >= f:
                lst.pop()

    # test each option in two possibilities


    def test_option(self):
        test = []
        if len(self.sorted) > 10:
            n = 10
        else:
            n = len(self.sorted)
        f = 1
        m = n + 1
        self.rec(test, m, n, f)

    # solve sudoku where only two possible values exists


    def solve_sudoku_2(self):
        self.sort_sudoku()
        self.test_option()


# run entire class and solve_sudoku
def solve_sudoku(sudoku, sudoku_copy):
    runner = Runner(sudoku, sudoku_copy)
    runner.solve_sudoku_1()
    runner.solve_sudoku_2()


# print using print_sudoku
def printer(sudoku):
    print_sudoku(sudoku)
