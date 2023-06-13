#!/usr/bin/python3

# get_input - get user input
# @n: line number to receive input for
# Return: list containing values that user has input


def get_input(n):
    # create list of accepted values
    accepted_input = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    # loop to run until correct input is received
    while True:
        print(f"Enter entire 9 digits, each 3 digits separated", end=" ")
        print(f"by space. Use 0 if no value\nExample input: 603 000 950")
        line = input(f"Line {n}: ")
        # check if 9 values were received each 3 values separated by space
        if len(line) != 11:
            continue
        # store 9 values in list without space
        my_list = []
        for i in line:
            if i in accepted_input:
                my_list.append(int(i))
        # check if list length is 9 in case accepted values entered are not 9
        if len(my_list) == 9:
            status = True
            for i in range(1, 10):
                # check if any digit 1-9 is repeated
                if my_list.count(i) > 1:
                    status = False
        # exit loop if all requirements are met
            if status:
                break
    return my_list
