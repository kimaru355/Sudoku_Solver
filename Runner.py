#!/usr/bin/python3

from Irregular import Irregular
from print_sudoku import print_sudoku

"""
    Runner - runs the entire class
    @Irregular: parent class of Runner
"""


class Runner(Irregular):
    # solve sudoku where one possible value exists
    def solve_sudoku_1(self):
        self.done1 = False
        # solve until no changes are made and done1 is true
        while self.done1 is False:
            self.sudoku_parts()
            self.check_possibilities()
            self.solve_puzzle()
        self.sudoku_parts()
        self.irregular = self.check_irregular()
        status = True
        # check if sudoku is complete(no zero in sudoku)
        for i in range(9):
            for j in range(9):
                if self.sudoku[i][j] == 0:
                    status = False
        if status is True:
            # check if complete sudoku is irregular
            if self.irregular is False and self.done2 is False:
                # print only one answer is complete sudoku is all good
                print_sudoku(self.sudoku)
                self.complete = True
                self.done2 = True

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

    # restores sudoku to before testing
    def restore_sudoku(self):
        for i in range(9):
            for j in range(9):
                self.sudoku[i][j] = self.sudoku_copy[i][j]

    # test the option to check for irregularities
    def tester(self, lst):
        a = 0
        # restore to remove previous test
        self.restore_sudoku()
        for k in self.sorted:
            # insert option from sorted at k
            self.sudoku[int(k[0])][int(k[1])] = self.sorted[k][lst[a]]
            a += 1
            # lst contains options and a records how many inserted
            # since lst may be shorter than lenght of sorted, a is
            # used to quit when lst has been inserted
            if a == len(lst) - 1:
                break
        self.sudoku_parts()
        status = self.check_irregular()
        if status is True:
            return None
        else:
            self.solve_sudoku_1()
            if self.done2 is False and self.irregular is False:
                if self.count == 1:
                    self.two_1.append(lst)
                elif self.count == 2:
                    sef.two_2.appent(lst)
                elif self.count == 3:
                    self.two_3.append(lst)
                elif self.count == 4:
                    self.two_4.append(lst)
                elif self.count == 5:
                    self.two_5.append(lst)

    # rec - use recursion to create possible outcomes
    # @lst: list to store possibilities
    # @m: number of functions to run. Fixed
    # @n: number of recursions left. Reduces by 1
    # @f: number of funtions running. Increases by 1
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
        lst = []
        if len(self.sorted) > 10:
            n = 10
        else:
            n = len(self.sorted)
        f = 1
        m = n + 1
        limit = len(self.sorted)
        if limit > 0:
            limit = limit // 10
            if limit > 5:
                limit = 5
        while self.done2 is False and len(self.sorted) > 0:
            self.count += 1
            self.rec(lst, m, n, f)
            if self.count == limit:
                break
            break

    # solve sudoku where only two possible values exists
    def solve_sudoku_2(self):
        self.sort_sudoku()
        self.test_option()
        print(len(self.sorted))
        if self.done2 is False:
            print("Unable to solve")
