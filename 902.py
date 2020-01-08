"""
Advent of Code 2019 - Day 9

Introduction

Author: Tom Kite
"""

file_name = "901.dat"


class int_code():
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

    def data_at(self, ind, mode):
        if (mode == "0"):
            return self.code[self.code[ind]]
        elif(mode == "1"):
            return self.code[ind]
        elif(mode == "2"):
            return self.code[self.relative_base + self.code[ind]]
        else:
            raise Exception("Invalid mode type %s in data_at" % mode)
        return

    def set_data(self, ind, mode, val):
        if (mode == "0"):
            self.code[self.code[ind]] = val
        elif(mode == "2"):
            self.code[self.relative_base + self.code[ind]] = val
        else:
            raise Exception("Invalid mode type %s in set_data" % mode)
        return

    def _code1(self, mode):
        val = self.data_at(self.index+1, mode[0]) +\
              self.data_at(self.index+2, mode[1])
        self.set_data(self.index+3, mode[2], val)
        self.index += 4
        return

    def _code2(self, mode):
        val = self.data_at(self.index+1, mode[0]) *\
              self.data_at(self.index+2, mode[1])
        self.set_data(self.index+3, mode[2], val)
        self.index += 4
        return

    def _code3(self, mode="0"):
        self.set_data(self.index+1, mode[0], self.ID)
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
            self.set_data(self.index+3, mode[2], 1)
        else:
            self.set_data(self.index+3, mode[2], 0)
        self.index += 4
        return

    def _code8(self, mode):
        if (self.data_at(self.index+1, mode[0]) == self.data_at(self.index+2, mode[1])):
            self.set_data(self.index+3, mode[2], 1)
        else:
            self.set_data(self.index+3, mode[2], 0)
        self.index += 4
        return

    def _code9(self, mode):
        self.relative_base += self.data_at(self.index+1, mode[0])
        self.index += 2
        return

    def _code99(self, mode=None):
        self.success = True
        return

    def run(self):
        while(self.success is None):
            self.iterations += 1
            opcode, mode = get_opcode(self.code[self.index])
            #print("Opcode: %s, mode: %s" % (opcode, mode))
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


def get_opcode(input_code, expected_len=5):
    input_code = str(input_code)
    if (len(input_code) > expected_len):
        raise Exception("Opcode is longer than expected length!")
    while (len(input_code) != expected_len):
        input_code = "0" + input_code
    return input_code[-2:], input_code[:-2][::-1]


def read_data(file_name):
    with open(file_name) as input_file:
        output = [int(x) for x in input_file.readline().split(',')]
    return output


if __name__ == "__main__":
    input_file = read_data(file_name)
    input_file = input_file + [0]*1000
    my_int_code = int_code(input_file, 2)
    my_int_code.run()
    my_int_code.show()
