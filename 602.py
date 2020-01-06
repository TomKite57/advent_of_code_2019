"""
Advent of Code 2019 - Day 6

This code will read in some puzzle input and find the minimal path between
YOU and SAN

Author: Tom Kite
"""

file_name = "601.dat"
orbits = {}
input_data = []


def read_file(file_name):
    with open(file_name, "r") as input_file:
        input_data = [x.rstrip("\n") for x in input_file]
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
