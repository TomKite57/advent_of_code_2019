"""
Advent of Code 2019 - Day 1

This program will read in data from a .dat file, and interpret this as an opcode

The program will run the opcode and return the first entry

Author: Tom Kite
"""

# Import statements
import sys

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

def op_code_act(index):
    global op_code
    if op_code[index] == 1:
        op_code_add(op_code[index+1],op_code[index+2],op_code[index+3])
        return
    elif op_code[index] == 2:
        op_code_mult(op_code[index+1],op_code[index+2],op_code[index+3])
        return
    elif op_code[index] == 99:
        return
    else:
        print("Invalid entry found in op_code!")
        sys.exit()

# Main program
def main_loop():
    
    global op_code
    
    # Main variables    
    file_name = "201.dat"
    
    # Check file open
    try:
        input_file = open(file_name,'r')
    except:
        print("File couldn't be opened!")
        return
    
    # Read in raw data, casting to float
    for line in input_file:
        for entry in line.split(','):
            op_code.append( int(entry) )
    
    # Close input file 
    input_file.close()
    
    for i in range(0,len(op_code),4):
        if op_code[i] == 99:
            break
        else:
            op_code_act(i)
    
    print(op_code)

main_loop()