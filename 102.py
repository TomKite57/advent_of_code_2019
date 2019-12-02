"""
Advent of Code 2019 - Day 1

This program will read in data from a .dat file, run the desired calculation 
and sum the results

Then the exrta fuel mass will be added to them results, and the process
will be rpeated

Author: Tom Kite
"""

import numpy as np

def calc_101(x):
    output = np.floor(x/3) - 2
    return output

def new_fuel_mass(current_masses):
    return sum(calc_101(current_masses))

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
    
    total_fuel_per_module = np.array([])
    
    for module_mass in raw_data:
        
        fuel_masses = np.array( [calc_101(module_mass)] )
        
        while ( calc_101(fuel_masses[-1]) > 0):
            fuel_masses = np.append( fuel_masses, calc_101(fuel_masses[-1]) )
        
        total_fuel_per_module = np.append( total_fuel_per_module, sum(fuel_masses) )
    
    print( sum(total_fuel_per_module) )
    
main_loop()