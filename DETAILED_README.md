The Sudoku solver solves sudoku puzzle by:
1. Splitting sudoku to obtain 9 squares and 9 vertical lines. The rules state that each number(1-9) cannot repeat in vertical line, horizontal line or one of the 9 small squares.
2. Checking numbers that can fit in each position and add the possible numbers in a 3D array. The list will be similar to sudoku except instead of 0s there will be an array of possible numbers that can fit in that position.
3. Adding all numbers that only one possible number can fit in a position
4. If sudoku is fully solved after the previous step, print it and skip the rest of the procedures
5. Create a dictionary containing address and numbers which only two possible numbers can fit in a position
6. Create 2^10 possibilities of the first 10 values in the dictionary
7. Test each for irregularity, if not irregular, repeat step 3 and 4 and if it fails, go to the next possibility.
8. After all 2^10 possibilities have been tried and none worked, tell user "Unable to solve sudoku"


All Good:
1. The Sudoku Solver can solve beginner and medium level sudoku puzzles.


Problems:
1. Since there are only two methods for solving, sudoku puzzles whose positions with one or two possible numbers are less(in advanced sudoku puzzles) cannot be solved.


Next Destination:
1. Add solving three posibilities positions after two has failed
2. Solve two possibilities positions when there are more than 10 two-possibilities positions

Skills used:
	Python:
		Intro upto Inheritance

# Anyone wishing to contribute, start from scratch or improve this, feel free to reach out
# I am keeping my test data(get_sudoku) with 12 sudoku puzzles to make it easier to identify current problem.
