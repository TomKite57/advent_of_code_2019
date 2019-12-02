"""
Advent of Code 2019 - Day 1

This program will read in data from a .dat file, run the desired calculation 
and sum the results

Author: Tom Kite
"""

import numpy as np

def calc_101(x):
    output = np.floor(x/3) - 2
    return output

def main_loop():
    
    # Main variables    
    file_name = "101.dat"
    raw_data = np.array([])
    
    # Check file open
    try:
        input_file = open(file_name,'r')
    except:
        print("File couldn't be opened!")
        return
    
    # Read in raw data, casting to float
    for line in input_file:
        raw_data = np.append( raw_data, float(line) )
    
    # Close input file 
    input_file.close()

    # Run calculation
    data = calc_101(raw_data)
    
    print(sum(data))
    
main_loop()