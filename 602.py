"""
Advent of Code 2019 - Day 6

This code will read in some puzzle input and find the total number of
direct and indirect orbits

Author: Tom Kite
"""

from numpy import genfromtxt

file_name = "601.dat"
orbits = {}
inverse_orbits = {}


class Path:
    bodies = []
    orbits = {}
    inverse_orbits = {}

    def __init__(self, starting_list, input_orbits, input_inverse_orbits):
        self.bodies = starting_list
        self.orbits = input_orbits
        self.inverse_orbits = input_inverse_orbits

    def see_possibilities(self):
        current_body = self.bodies[-1]
        output = []
        if current_body in self.orbits:
            for body in self.orbits[current_body]:
                output.append(body)
        if current_body in self.inverse_orbits:
            for body in self.inverse_orbits[current_body]:
                output.append(body)
        return output

    def take_all_steps(self):
        path_list = []
        for move in self.see_possibilities():
            new_path = Path(self.bodies+[move], self.orbits, self.inverse_orbits)
            if (not new_path.does_path_repeat()):
                path_list.append(new_path)
        return path_list

    def does_path_repeat(self):
        for body in self.bodies:
            if (self.bodies.count(body) > 1):
                return True
        return False

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
    inverse_orbits[bodyA] = bodyB

san_orbit = orbits["SAN"]
san_path = [san_orbit]
while (san_path[-1] != "COM"):
    san_path.append(orbits[san_path[-1]])

my_orbit = orbits["YOU"]
my_path = [my_orbit]
while (my_path[-1] != "COM"):
    my_path.append(orbits[my_path[-1]])

# Find coincidences
distances = []
for my_obj in my_path:
    if (san_path.count(my_obj) != 0):
        my_dist = my_path.index(my_obj)
        san_dist = san_path.index(my_obj)
        distances.append(my_dist + san_dist)

print(distances)
print(min(distances))
