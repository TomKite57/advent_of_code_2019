"""
Advent of Code 2019 - Day 6

This code will read in some puzzle input and find the minimal path between
YOU and SAN

Author: Tom Kite
"""

import sys

file_name = "601.dat"
orbits = {}


def read_file(file_name):
    try:
        open_file = open(file_name, 'r')
    except IOError:
        print("Couldn't open file: %s" % file_name)
        sys.exit()

    input_data = [x.rstrip("\n") for x in open_file]
    return input_data


def get_path_to(body, orbits):
    path = [body]
    while (path[-1] != "COM"):
        path.append(orbits[path[-1]])
    return path


if __name__ == "__main__":

    input_data = read_file(file_name)

    for line in input_data:
        bodyA, bodyB = line.split(")")
        orbits[bodyB] = bodyA

    san_path = get_path_to(orbits["SAN"], orbits)
    my_path = get_path_to(orbits["YOU"], orbits)

    for body in my_path:
        if (body in san_path):
            last_coincidence = body
            break

    my_dist = my_path.index(last_coincidence)
    san_dist = san_path.index(last_coincidence)
    print(my_dist + san_dist)
