"""
Advent of Code 2019 - Day 1

This program will read in data from a .dat file, and interpret this as an opcode

The program will run the opcode and return the first entry

Author: Tom Kite
"""

# Import statements
import sys
import copy

# Global variable
op_code = []

# Functions to intepret opcodes
def op_code_add(entry1,entry2,entry3):
    global op_code
    op_code[entry3] = op_code[entry1] + op_code[entry2]
    return

def op_code_mult(entry1,entry2,entry3):
    global op_code
    op_code[entry3] = op_code[entry1] * op_code[entry2]
    return

def get_op_code(file_name):
    global op_code
    # Check file open
    try:
        input_file = open(file_name,'r')
    except:
        print("File couldn't be opened!")
        sys.exit()
    
    # Read in raw data, casting to float
    for line in input_file:
        for entry in line.split(','):
            op_code.append( int(entry) )
    
    # Close input file 
    input_file.close()
    return

def set_new_param(entry1,entry2):
    global op_code
    op_code[1] = entry1
    op_code[2] = entry2
    return

def run_op_code():
    global op_code
    for index in range(0,len(op_code),4):
        if op_code[index] == 1:
            op_code_add(op_code[index+1],op_code[index+2],op_code[index+3])
        elif op_code[index] == 2:
            op_code_mult(op_code[index+1],op_code[index+2],op_code[index+3])
        elif op_code[index] == 99:
            return True
        else:
            #print("Invalid entry found in op_code!")
            return False
    return False

# Main program
def main_loop():
    
    global op_code
    
    get_op_code("201.dat")
    
    input_code = copy.deepcopy(op_code)
    
    for i in range(0,100):
        for j in range(0,100):
            op_code = copy.deepcopy(input_code)
            set_new_param(i,j)
            valid_result = run_op_code()
            
            if (valid_result and op_code[0] == 19690720):
                print ("Found the right noun and verb!: " + str(i) + ", " + str(j))
                print ("Answer: " + str(100*i + j))
                return
            

main_loop()