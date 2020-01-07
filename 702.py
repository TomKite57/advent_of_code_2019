"""
Advent of Code 2019 - Day 7

Introduction

Author: Tom Kite
"""

from itertools import permutations
import copy

file_name = "701.dat"
PHASE_SETTINGS = range(5, 10)
NUM_OF_THRUSTERS = 5


class int_code():
    code = []
    success = None
    ID = None
    return_value = None
    index = 0
    iterations = 0
    guide = {}

    def __init__(self, input_code=[], input_ID=0):
        self.code = input_code
        self.ID = input_ID
        self.index = 0
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
        self.code[self.code[self.index+1]] = int(self.ID[0])
        self.ID.pop(0)
        self.index += 2
        return

    def _code4(self, mode):
        self.return_value = self.data_at(self.index+1, mode[0])
        self.index += 2
        self.success = True
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
        self.success = "99"
        return

    def run(self):
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
        print("Input ID: %s" % self.ID)
        return


def get_opcode(input_code, expected_len=4):
    input_code = str(input_code)
    if (len(input_code) > expected_len):
        raise Exception("Opcode is longer than expected length!")
    while (len(input_code) != expected_len):
        input_code = "0" + input_code
    return input_code[2:], input_code[:2][::-1]


def read_data(file_name):
    with open(file_name) as input_file:
        output = [int(x) for x in input_file.readline().split(',')]
    return output


def run_feedback_circuit(program, phases):
    current_signal = 0
    thrusters = [int_code(copy.copy(program), [phase]) for phase in phases]

    while (thrusters[-1].success != "99"):
        for thruster in thrusters:
            thruster.ID.append(current_signal)
            thruster.run()
            current_signal = thruster.return_value
    return current_signal


if __name__ == "__main__":
    input_file = read_data(file_name)
    phase_combinations = permutations(PHASE_SETTINGS)
    results = {}

    for phases in phase_combinations:
        signal = run_feedback_circuit(input_file, phases)
        results[phases] = signal

    maxID = max(results, key=results.get)
    print("Max value found at %s with %s" % (maxID, results[maxID]))
