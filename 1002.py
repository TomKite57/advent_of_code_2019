"""
Advent of Code 2019 - Day 10

Introduction

Author: Tom Kite
"""

import copy
import math
import matplotlib.pyplot as plt

file_name = "1001.dat"


class coord:
    layer = -1

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

    def angle(self):
        if (self.x == 0 and self.y > 0):
            return 270-90
        elif (self.x == 0 and self.y < 0):
            return 90-90
        degrees = math.degrees(math.atan2(self.y, self.x))-270
        while degrees < 0:
            degrees += 360
        return round(degrees)


def read_file(file_name):
    output_data = []
    with open(file_name) as input_file:
        for line in input_file:
            row = list(line)
            if (row[-1] == "\n"):
                row.pop()
            output_data.append(row)
    return output_data


def list_to_string(input_list):
    string = ""
    for element in input_list:
        string += str(element)
    return string


def find_asteroids(input_data):
    asteroids = []
    for y in range(len(input_data)):
        for x in range(len(input_data[y])):
            if (input_data[y][x] == '#'):
                asteroids.append(coord(x, y))
    return asteroids


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


def get_eq_classes(asteroid_list, origin):
    eq_classes = []
    for asteroid in asteroid_list:
        if asteroid == origin:
            continue
        class_exist = False
        for eq_class in eq_classes:
            if eq_rel(asteroid, eq_class[0], origin):
                class_exist = True
                eq_class.append(asteroid)
                break
        if not class_exist:
            eq_classes.append([asteroid])
    return eq_classes


def generate_image(input_data, max_loc):
    image = copy.deepcopy(input_data)
    for y in range(len(image)):
        for x in range(len(image[y])):
            if (image[y][x] == "."):
                image[y][x] = 0
            elif (image[y][x] == "#"):
                image[y][x] = 1

    image[max_loc.y][max_loc.x] = 2

    plt.imshow(image)
    return


if __name__ == "__main__":
    input_data = read_file(file_name)
    asteroids = find_asteroids(input_data)

    max_roids = 0
    max_roids_loc = coord()

    for asteroid in asteroids:
        eq_classes = get_eq_classes(asteroids, asteroid)
        visible_asteroids = len(eq_classes)
        if (visible_asteroids > max_roids):
            max_roids = visible_asteroids
            max_roids_loc = asteroid

    print("%i asteroids visible from (%i,%i)"
          % (max_roids, max_roids_loc.x, max_roids_loc.y))

    eq_classes = get_eq_classes(asteroids, max_roids_loc)

    eq_classes = sorted(eq_classes, key=lambda x: (x[0]-max_roids_loc).angle())

    for i in range(len(eq_classes)):
        eq_classes[i] = sorted(eq_classes[i], key=lambda x:
                               (x-max_roids_loc).manhat_dist())

    for i in range(len(eq_classes)):
        for j in range(len(eq_classes[i])):
            ast = eq_classes[i][j]
            ast.layer = j+1

    asteroids = sorted(asteroids, key=lambda x:
                       1000*x.layer + (x-max_roids_loc).angle())

    print("200th asteroid to be destroyed is at (%i,%i)"
          % (asteroids[200].x, asteroids[200].y))
