"""
Advent of Code 2019 - Day 13

Introduction

Author: Tom Kite
"""

from copy import deepcopy
from matplotlib.pyplot import imshow

FILE_NAME = "1301.dat"
INPUT_GUIDE = {
        'a': -1,
        's': 0,
        'd': +1
        }


def read_file(file_name):
    with open(file_name, 'r') as input_file:
        output = [int(x) for x in input_file.readline().split(',')]
    return output


def list_to_string(input_list):
    string = ""
    for element in input_list:
        string += str(element)
    return string


def sign(num):
    if num > 0:
        return +1
    elif num < 0:
        return -1
    else: 
        return 0


def count_instance(grid, char):
    count = 0
    for row in grid:
        count += row.count(char)
    return count


def get_opcode(input_code, expected_len=5):
    input_code = str(input_code)
    if (len(input_code) > expected_len):
        raise Exception("Opcode is longer than expected length!")
    while (len(input_code) != expected_len):
        input_code = "0" + input_code
    return input_code[-2:], input_code[:-2][::-1]


class int_code_computer():
    def __init__(self, input_code, input_ID):
        self.code = input_code
        self.ID = input_ID
        self.relative_base = 0
        self.iterations = 0
        self.index = 0
        self.return_value = None
        self.success = None
        self.guide = {
                "01": self._code1,
                "02": self._code2,
                "03": self._code3,
                "04": self._code4,
                "05": self._code5,
                "06": self._code6,
                "07": self._code7,
                "08": self._code8,
                "09": self._code9,
                "99": self._code99,
                }
        return

    def extend_code(self, desired_index):
        difference = desired_index - len(self.code) + 1
        if (difference > 0):
            self.code += [0] * difference
        return

    def get_data(self, ind, mode):
        if (mode == "0"):
            self.extend_code(self.code[ind])
            return self.code[self.code[ind]]
        elif(mode == "1"):
            self.extend_code(ind)
            return self.code[ind]
        elif(mode == "2"):
            self.extend_code(self.relative_base + self.code[ind])
            return self.code[self.relative_base + self.code[ind]]
        else:
            raise Exception("Invalid mode type %s in get_data" % mode)
        return

    def set_data(self, ind, mode, val):
        if (mode == "0"):
            self.extend_code(self.code[ind])
            self.code[self.code[ind]] = val
        elif(mode == "2"):
            self.extend_code(self.relative_base + self.code[ind])
            self.code[self.relative_base + self.code[ind]] = val
        else:
            raise Exception("Invalid mode type %s in set_data" % mode)
        return

    def _code1(self, mode):
        val = self.get_data(self.index+1, mode[0]) +\
              self.get_data(self.index+2, mode[1])
        self.set_data(self.index+3, mode[2], val)
        self.index += 4
        return

    def _code2(self, mode):
        val = self.get_data(self.index+1, mode[0]) *\
              self.get_data(self.index+2, mode[1])
        self.set_data(self.index+3, mode[2], val)
        self.index += 4
        return

    def _code3(self, mode="0"):
        """
        # Take input from user, corresponding to joystick position
        user_input = 0
        while (user_input not in INPUT_GUIDE.keys()):
            user_input = input("Input: ")
        self.ID = INPUT_GUIDE[user_input]
        """
        self.set_data(self.index+1, mode[0], self.ID)
        self.index += 2
        return

    def _code4(self, mode):
        self.return_value = self.get_data(self.index+1, mode[0])
        self.index += 2
        self.success = True
        return

    def _code5(self, mode):
        if (self.get_data(self.index+1, mode[0]) != 0):
            self.index = self.get_data(self.index+2, mode[1])
            return
        self.index += 3
        return

    def _code6(self, mode):
        if (self.get_data(self.index+1, mode[0]) == 0):
            self.index = self.get_data(self.index+2, mode[1])
            return
        self.index += 3
        return

    def _code7(self, mode):
        if (self.get_data(self.index+1, mode[0]) < self.get_data(self.index+2, mode[1])):

            self.set_data(self.index+3, mode[2], 1)
        else:
            self.set_data(self.index+3, mode[2], 0)
        self.index += 4
        return

    def _code8(self, mode):
        if (self.get_data(self.index+1, mode[0]) == self.get_data(self.index+2, mode[1])):
            self.set_data(self.index+3, mode[2], 1)
        else:
            self.set_data(self.index+3, mode[2], 0)
        self.index += 4
        return

    def _code9(self, mode):
        self.relative_base += self.get_data(self.index+1, mode[0])
        self.index += 2
        return

    def _code99(self, mode=None):
        self.success = "99"
        return

    def run(self):
        if (self.success is not False):
            self.success = None

        while(self.success is None):
            self.iterations += 1
            opcode, mode = get_opcode(self.code[self.index])
            if opcode in self.guide:
                self.guide[opcode](mode)
            else:
                self.success = False
        return

    def show(self):
        print("Successful run: %s" % self.success)
        print("Result: %s" % self.return_value)
        print("Code at 0: %s" % self.code[0])
        print("Number of iterations: %s" % self.iterations)
        return


class arcade_game():
    def __init__(self, code, inputs_to_try):
        self.computer = int_code_computer(code, 0)
        grid_x, grid_y = self.predict_grid_size(code)
        self.grid = [[0 for x in range(grid_x)] for y in range(grid_y)]
        self.inputs = inputs_to_try
        self.score = 0
        # AI variables
        self.ball_x = -1
        self.paddle_x = -1
        return

    def predict_grid_size(self, code):
        trial_computer = int_code_computer(deepcopy(code), 0)
        max_x = 0
        max_y = 0
        while(trial_computer.success != "99"):
            trial_computer.run()
            max_x = max(trial_computer.return_value, max_x)
            trial_computer.run()
            max_y = max(trial_computer.return_value, max_y)
            trial_computer.run()
        return max_x+1, max_y+1

    def run_game(self):
        while(self.computer.success != "99"):
            self.computer.run()
            temp_x = self.computer.return_value
            self.computer.run()
            temp_y = self.computer.return_value
            self.computer.run()
            tile = self.computer.return_value
            if tile in range(5):
                self.grid[temp_y][temp_x] = tile
                if (tile == 4):
                    self.ball_x = temp_x
                elif (tile == 3):
                    self.paddle_x = temp_x
            else:
                self.score = tile
            self.show_grid()
            self.computer.ID = sign(self.ball_x - self.paddle_x)

    def show_grid(self):
        for y in range(len(self.grid)):
            print(list_to_string(self.grid[y]))
        return

    def show_score(self):
        print("The score is %i" % self.score)
        return


if __name__ == "__main__":
    code = read_file(FILE_NAME)
    code[0] = 2
    game = arcade_game(code, [])
    game.run_game()
    game.show_grid()
    game.show_score()
    print(count_instance(game.grid, 2))
