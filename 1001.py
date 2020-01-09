"""
Advent of Code 2019 - Day 10

Introduction

Author: Tom Kite
"""

import copy

file_name = "1001.dat"


class coord:
    def __init__(self, x_val=0, y_val=0):
        self.x = x_val
        self.y = y_val

    def __add__(self, other):
        new_coord = coord(self.x + other.x, self.y + other.y)
        return new_coord

    def __sub__(self, other):
        new_coord = coord(self.x - other.x, self.y - other.y)
        return new_coord

    def __mul__(self, scalar):
        new_coord = coord(self.x * scalar, self.y * scalar)
        return new_coord

    def __eq__(self, other):
        if (self.x == other.x and self.y == other.y):
            return True
        else:
            return False

    def manhat_dist(self):
        return abs(self.x) + abs(self.y)

    def show(self):
        print("(%i,%i)" % (self.x, self.y))
        return

    def get_quad(self):
        if (self.x >= 0 and self.y > 0):
            return "quadTR"
        elif (self.x > 0 and self.y <= 0):
            return "quadBR"
        elif (self.x <= 0 and self.y < 0):
            return "quadBL"
        elif (self.x < 0 and self.y >= 0):
            return "quadTL"
        else:
            return "O"


def eq_rel(pointA, pointB, origin=coord()):
    relA = pointA - origin
    relB = pointB - origin
    if (relA.get_quad() != relB.get_quad()):
        return False
    if (relA.x == 0 or relB.x == 0 or relA.y == 0 or relB.y == 0):
        if (relA.x == 0 and relB.x == 0):
            return True
        elif (relA.y == 0 and relB.y == 0):
            return True
        else:
            return False
    else:
        x_ratio = relA.x / relB.x
        y_ratio = relA.y / relB.y
        return x_ratio == y_ratio


def read_file(file_name):
    output_data = []
    with open(file_name) as input_file:
        for line in input_file:
            row = list(line)
            if (row[-1] == "\n"):
                row.pop()
            output_data.append(row)
    return output_data


def find_asteroids(input_data):
    asteroids = []
    for y in range(len(input_data)):
        for x in range(len(input_data[y])):
            if (input_data[y][x] == '#'):
                asteroids.append(coord(x, y))
    return asteroids


def get_eq_classes(asteroid_list, origin):
    eq_classes = []
    for asteroid in asteroid_list:
        if asteroid == origin:
            continue
        class_exist = False
        for eq_class in eq_classes:
            if eq_rel(asteroid, eq_class, origin):
                class_exist = True
                break
        if not class_exist:
            eq_classes.append(asteroid)
    return eq_classes


def list_to_string(input_list):
    string = ""
    for element in input_list:
        string += str(element)
    return string


if __name__ == "__main__":
    input_data = read_file(file_name)
    asteroids = find_asteroids(input_data)
    output_data = copy.deepcopy(input_data)

    max_roids = 0
    max_roids_loc = coord()

    for asteroid in asteroids:
        eq_classes = get_eq_classes(asteroids, asteroid)
        visible_asteroids = len(eq_classes)
        output_data[asteroid.y][asteroid.x] = visible_asteroids
        if (visible_asteroids > max_roids):
            max_roids = visible_asteroids
            max_roids_loc = asteroid

    print(max_roids)
    max_roids_loc.show()
    
    for line in output_data:
        print(list_to_string(line))
