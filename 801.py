"""
Advent of Code 2019 - Day 8

Description

Author: Tom Kite
"""

from numpy import genfromtxt

file_name = "801.dat"
width = 25
height = 6
area = width*height

input_data = str(genfromtxt(file_name, dtype=str))

number_of_layers = int(len(input_data) / area)

layers = []
for i in range(number_of_layers):
    new_layer = input_data[i*area:(i+1)*area]
    layers.append(new_layer)

layers = sorted(layers, key=lambda x: x.count("0"), reverse=False)

print(layers[0].count("1") * layers[0].count("2"))
