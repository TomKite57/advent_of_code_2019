"""
Advent of Code 2019 - Day 5

Introduction

Author: Tom Kite
"""

file_name = "501.dat"


class int_code():
    code = []
    success = None
    ID = None
    return_value = None
    index = 0
    iterations = 0
    guide = {}

    def __init__(self, input_code, input_ID):
        self.code = input_code
        self.ID = input_ID
        self.guide = {
                "01": self._code1,
                "02": self._code2,
                "03": self._code3,
                "04": self._code4,
                "05": self._code5,
                "06": self._code6,
                "07": self._code7,
                "08": self._code8,
                "99": self._code99,
                }

    def data_at(self, ind, mode):
        if (mode == "0"):
            return self.code[self.code[ind]]
        elif(mode == "1"):
            return self.code[ind]
        else:
            raise Exception("Invalid mode type %s" % mode)
        return

    def _code1(self, mode):
        self.code[self.code[self.index+3]] = \
                                    self.data_at(self.index+1, mode[0]) +\
                                    self.data_at(self.index+2, mode[1])
        self.index += 4
        return

    def _code2(self, mode):
        self.code[self.code[self.index+3]] = \
                                    self.data_at(self.index+1, mode[0]) *\
                                    self.data_at(self.index+2, mode[1])
        self.index += 4
        return

    def _code3(self, mode=None):
        self.code[self.code[self.index+1]] = self.ID
        self.index += 2
        return

    def _code4(self, mode):
        self.return_value = self.data_at(self.index+1, mode[0])
        self.index += 2
        return

    def _code5(self, mode):
        if (self.data_at(self.index+1, mode[0]) != 0):
            self.index = self.data_at(self.index+2, mode[1])
            return
        self.index += 3
        return

    def _code6(self, mode):
        if (self.data_at(self.index+1, mode[0]) == 0):
            self.index = self.data_at(self.index+2, mode[1])
            return
        self.index += 3
        return

    def _code7(self, mode):
        if (self.data_at(self.index+1, mode[0]) < self.data_at(self.index+2, mode[1])):
            self.code[self.code[self.index+3]] = 1
        else:
            self.code[self.code[self.index+3]] = 0
        self.index += 4
        return

    def _code8(self, mode):
        if (self.data_at(self.index+1, mode[0]) == self.data_at(self.index+2, mode[1])):
            self.code[self.code[self.index+3]] = 1
        else:
            self.code[self.code[self.index+3]] = 0
        self.index += 4
        return

    def _code99(self, mode=None):
        self.success = True
        return

    def run(self):
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


def get_opcode(input_code):
    input_code = str(input_code)
    while (len(input_code) != 4):
        input_code = "0" + input_code
    return input_code[2:], input_code[:2][::-1]


def read_data(file_name):
    with open(file_name) as input_file:
        output = [int(x) for x in input_file.readline().split(',')]
    return output


if __name__ == "__main__":
    input_file = read_data(file_name)
    my_int_code = int_code(input_file, 5)
    my_int_code.run()
    my_int_code.show()
