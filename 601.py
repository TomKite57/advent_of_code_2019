"""
Advent of Code 2019 - Day 6

This code will read in some puzzle input and find the total number of
direct and indirect orbits

Author: Tom Kite
"""

from numpy import genfromtxt

file_name = "601.dat"
orbits = {}

def count_orbits_for_body(body_name, orbits):
    total_orbits = 0
    while (body_name != "COM"):
        body_name = orbits[body_name]
        total_orbits += 1
    return total_orbits
        

input_data = genfromtxt(file_name, dtype=str, delimiter="\n")

for line in input_data:
    index = line.find(")")
    bodyA = line[:index]
    bodyB = line[index+1:]

    orbits[bodyB] = bodyA

grand_total = 0

for body in orbits:
    grand_total += count_orbits_for_body(body, orbits)

print(grand_total)
