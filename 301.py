"""
Advent of Code 2019 - Day 3

This program will read in data from a .dat file, and save the instructions
as vertices of a wire rather than the instructions

Author: Tom Kite
"""

import numpy as np
import sys

class coord:
    x = 0
    y = 0
    
    def __init__(self, x_val=0, y_val=0):
        self.x = x_val
        self.y = y_val
        
    def __add__(self,other):
        new_coord = coord(self.x + other.x, self.y + other.y)
        return new_coord
    
    def __mul__(self,scalar):
        new_coord = coord(self.x * scalar, self.y * scalar)
        return new_coord
    
    def manhat_dist(self):
        return abs(self.x) + abs(self.y)

guide = {
        "R": coord(1,0),
        "L": coord(-1,0),
        "U": coord(0,1),
        "D": coord(0,-1)
        }

def input_to_coords(instructions):
    output = [ coord() ]
    for step in instructions:
        coord_step = guide[step[0]] * int(step[1:])
        output.append( output[-1] + coord_step )
    return output

def read_data(filename):
    try:
        inputA, inputB = np.genfromtxt(filename, dtype = str, delimiter = ',')
    except:
        print("Data file could not be opened/interpreted")
        sys.exit()
    outputA, outputB = input_to_coords(inputA), input_to_coords(inputB)
    return outputA, outputB

def do_wires_cross(coordA,coordB,coordX,coordY):
    if (coordA.x == coordB.x):
        # AB runs up/down
        if (  (coordA.y < coordX.y < coordB.y or coordB.y < coordX.y < coordA.y)
        and ( coordX.x < coordA.x < coordY.x or coordY.x < coordA.x < coordX.x ) ):
            return True, coord(coordA.x, coordX.y)
        else:
            return False, coord()
    elif(coordX.x == coordY.x):
        return do_wires_cross(coordX,coordY,coordA,coordB)
    else:
        return False, coord()
        

wireA, wireB = read_data("301.dat")

cross_list = []
for i in range( len(wireA)-1 ):
    for j in range( len(wireB)-1 ):
        tempBool, temp_coord = do_wires_cross( wireA[i], wireA[i+1], wireB[j], wireB[j+1] )
        if (tempBool):
            cross_list.append( temp_coord )

cross_list = sorted(cross_list, key=lambda x: x.manhat_dist(), reverse=False)

print( cross_list[0].manhat_dist() )

