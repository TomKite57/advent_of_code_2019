"""
Advent of Code 2019 - Day 5

Introduction

Author: Tom Kite
"""

from numpy import genfromtxt
import sys

file_name = "501.dat"

"""
class int_code:
    code = []
    success = None
    ID = 0

    def __init__(self, input_code=99, input_ID=1):
        self.code = input_code
        self.ID = input_ID

    def _add(self, entry1, entry2, entry3):
        self.code[entry3] = self.code[entry1] + self.code[entry2]
        return

    def _mult(self, entry1, entry2, entry3):
        self.code[entry3] = self.code[entry1] * self.code[entry2]
        return

    def _input(self, entry):
        self.code[entry] = self.ID
        return

    def _output(self, entry):
        self.code[0] = self.code[entry]
        return

    def run(self):
        index = 0
        while(0 <= index < len(self.code)):
            if self.code[index] == 1:
                self._add(self.code[index+1],
                          self.code[index+2],
                          self.code[index+3])
                index += 4
            elif self.code[index] == 2:
                self._mult(self.code[index+1],
                           self.code[index+2],
                           self.code[index+3])
                index += 4
            elif self.code[index] == 3:
                self._input(self.code[index+1])
                index += 2
            elif self.code[index] == 4:
                self._output(self.code[index+1])
                return
            elif self.code[index] == 99:
                self.success = True
                return
            else:
                self.success = False
                return
        self.success = False
        return

    def show(self):
        print("Successful run: %s" % self.success)
        print("Result: %s" % self.code[0])
        return
"""


def split_op_code(op_code):
    op_code = str(op_code)
    run_mode = op_code[3:]
    op_code = op_code[:len(op_code)-2]
    if (run_mode == "01" or run_mode == "02"):
        # Expect 3 modes
        mode_1 = op_code[-1]
        mode_2 = op_code[-2]
        mode_3 = op_code[-3]
        return run_mode, mode_1, mode_2, mode_3
    elif (run_mode == "03" or run_mode == "04"):
        # Expect 1 mode
        mode_1 = op_code[-1]
        return run_mode, None, None, mode_1
    elif (run_mode == "99"):
        return run_mode, None, None, None
    else:
        # Something has gone wrong
        print("Unable to interpret op code")
        sys.exit()


class int_code:
    code = []
    success = None
    ID = 0
    run_counter = 0
    return_value = None
    index=0

    def __init__(self, input_code=99, input_ID=1):
        self.code = input_code
        self.ID = input_ID

    def _add(self, param1, param2, param3, mode="00"):
        if (mode[0] == "0"): param2 = self.code[param2]
        if (mode[1] == "0"): param3 = self.code[param3]
        self.code[param1] = param2 + param3
        return

    def _mult(self, param1, param2, param3, mode="00"):
        if (mode[0] == "0"): param2 = self.code[param2]
        if (mode[1] == "0"): param3 = self.code[param3]
        self.code[param1] = param2 * param3
        return

    def _input(self, param):
        self.code[param] = self.ID
        return

    def _output(self, param, mode="0"):
        if (mode == "0"): param = self.code[param]
        self.return_value = param
        return
    
    def _rule5(self, param1, param2, param3, mode="00"):
        if (mode[0] == "0"): param2 = self.code[param2]
        if (mode[1] == "0"): param3 = self.code[param3]
        if (param2 != "0"):
            self.code[param1] = param3
        return
    
    def _rule6(self, param1, param2, param3, mode="00"):
        if (mode[0] == "0"): param2 = self.code[param2]
        if (mode[1] == "0"): param3 = self.code[param3]
        if (param2 == "0"):
            self.code[param1] = param3
        return
    
    def _rule7(self, param1, param2, param3, mode="00"):
        if (mode[0] == "0"): param2 = self.code[param2]
        if (mode[1] == "0"): param3 = self.code[param3]
        if (param2 < param3):
            self.code[param1] = 1
        else:
            self.code[param1] = 0
        return
    
    def _rule8(self, param1, param2, param3, mode="00"):
        if (mode[0] == "0"): param2 = self.code[param2]
        if (mode[1] == "0"): param3 = self.code[param3]
        if (param2 == param3):
            self.code[param1] = 1
        else:
            self.code[param1] = 0
        return

    def run(self):
        self.index = 0
        while(0 <= self.index < len(self.code)):
            self.run_counter += 1

            op_code = str(self.code[self.index])
            while (len(op_code) != 5):
                op_code = "0" + op_code

            code_1 = op_code[0]
            code_3 = op_code[1]
            code_2 = op_code[2]
            run_code = op_code[3:]

            if (run_code == "01"):
                param1 = self.code[self.index+3]
                param2 = self.code[self.index+1]
                param3 = self.code[self.index+2]
                self._add(param1, param2, param3, code_2 + code_3)
                self.index += 4
            elif (run_code == "02"):
                param1 = self.code[self.index+3]
                param2 = self.code[self.index+1]
                param3 = self.code[self.index+2]
                self._mult(param1, param2, param3, code_2 + code_3)
                self.index += 4
            elif (run_code == "04"):
                param = self.code[self.index+1]
                #if (code_2 == "0"): param = self.code[self.code[index+1]]
                self._output(param, code_2)
                self.index += 2
            elif (run_code == "03"):
                param = self.code[self.index+1]
                self._input(param)
                self.index += 2
            elif (run_code == "05"):
                param1 = self.code[self.index+3]
                param2 = self.code[self.index+1]
                param3 = self.code[self.index+2]
                self._rule5(param1, param2, param3, code_2 + code_3)
                self.index += 4
            elif (run_code == "06"):
                param1 = self.code[self.index+3]
                param2 = self.code[self.index+1]
                param3 = self.code[self.index+2]
                self._rule5(param1, param2, param3, code_2 + code_3)
                self.index += 4
            elif (run_code == "07"):
                param1 = self.code[self.index+3]
                param2 = self.code[self.index+1]
                param3 = self.code[self.index+2]
                self._rule5(param1, param2, param3, code_2 + code_3)
                self.index += 4
            elif (run_code == "08"):
                param1 = self.code[self.index+3]
                param2 = self.code[self.index+1]
                param3 = self.code[self.index+2]
                self._rule5(param1, param2, param3, code_2 + code_3)
                self.index += 4
            elif (run_code == "99"):
                print("Exits with code 99")
                self.success = True
                return
            else:
                print ("Bad op_code")
                self.success = False
                return

        self.success = False
        return

    def show(self):
        print("Successful run: %s" % self.success)
        print("Code at 0: %s" % self.code[0])
        print("Return value: %s" % self.return_value)
        print("Run consisted of %s steps" % self.run_counter)
        return

#############
# MAIN LOOP #
#############


input_file = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]#genfromtxt(file_name, dtype=int, delimiter=",")

my_int_code = int_code(input_file, 5)

#print(my_int_code.code)

my_int_code.run()

my_int_code.show()
