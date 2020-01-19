"""
Advent of Code 2019 - Day 9

Introduction

Author: Tom Kite
"""

from matplotlib.pyplot import imshow
from copy import deepcopy

file_name = "1101.dat"


def read_data(file_name):
    with open(file_name) as input_file:
        output = [int(x) for x in input_file.readline().split(',')]
    return output


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

    def exted_code(self, desired_index):
        difference = desired_index - len(self.code) + 1
        if (difference > 0):
            self.code += [0] * difference
        return

    def get_data(self, ind, mode):
        if (mode == "0"):
            self.exted_code(self.code[ind])
            return self.code[self.code[ind]]
        elif(mode == "1"):
            self.exted_code(ind)
            return self.code[ind]
        elif(mode == "2"):
            self.exted_code(self.relative_base + self.code[ind])
            return self.code[self.relative_base + self.code[ind]]
        else:
            raise Exception("Invalid mode type %s in get_data" % mode)
        return

    def set_data(self, ind, mode, val):
        if (mode == "0"):
            self.exted_code(self.code[ind])
            self.code[self.code[ind]] = val
        elif(mode == "2"):
            self.exted_code(self.relative_base + self.code[ind])
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


def rotate(pointing, direction):
    values = ["U", "R", "D", "L"]
    if (direction == 0):
        return values[values.index(pointing) - 1]
    elif (direction == 1):
        return values[values.index(pointing) - 3]
    else:
        raise Exception("Invalid rotation value %s found" % direction)


class paint_robot():
    def __init__(self, int_code, grid_size):
        self.computer = int_code_computer(int_code, 1)
        self.x = 10
        self.y = 10
        self.grid = [[0 for x in range(grid_size)] for y in range(grid_size)]
        self.grid[self.y][self.x] = 1
        self.painted_squares = set()
        self.pointing = "U"
        return

    def move(self):
        if (self.pointing == "U"):
            self.y -= 1
        elif (self.pointing == "R"):
            self.x += 1
        elif (self.pointing == "D"):
            self.y += 1
        elif (self.pointing == "L"):
            self.x -= 1
        else:
            raise Exception("Invalid pointer %s found" % self.pointing)
        return

    def run_computer(self):
        while (self.computer.success != "99"):
            # Find paint number
            self.computer.run()
            self.grid[self.y][self.x] = self.computer.return_value
            self.painted_squares.add((self.x, self.y))

            # Find move direction
            self.computer.run()
            self.pointing = rotate(self.pointing, self.computer.return_value)
            self.move()
            self.computer.ID = deepcopy(self.grid[self.y][self.x])
        return


if __name__ == "__main__":
    input_file = read_data(file_name)
    my_robot = paint_robot(input_file, 100)
    my_robot.run_computer()
    imshow(my_robot.grid)
