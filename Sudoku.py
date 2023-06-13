#!/usr/bin/python3

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
        self.done2 = False
        self.sorted = {}
        self.irregular = False
        self.two_1 = []
        self.two_2 = []
        self.two_i = []
        self.two_4 = []
        self.two_5 = []
        self.count = 0
        self.complete = False

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
