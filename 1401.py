"""
Advent of Code 2019 - Day 14

Introduction

Author: Tom Kite
"""

FILE_NAME = "1401.dat"


class element():
    def __init__(self, tup):
        self.name = tup[1]
        self.quantity = tup[0]

    def __add__(self, other):
        if (self.name == other.name):
            return element(self.quantity + other.quantity, self.name)
        else:
            return None

    def __eq__(self, other):
        return (self.name == other.name)

    def show(self):
        print("%i of type %s" % (self.quantity, self.name))

    def get_tup(self):
        return (self.quantity, self.name)


def read_file(file_name):
    recipes = {}
    with open(file_name, 'r') as input_file:
        reactions = [x.strip() for x in input_file]

    for line in reactions:
        line = line.split(" => ")
        left_line = line[0].split(", ")

        LHS = []
        for segment in left_line:
            segment = segment.split(" ")
            LHS.append((int(segment[0]), segment[1]))

        right_line = line[1].split(" ")
        RHS = (int(right_line[0]), right_line[1])
        recipes[RHS] = LHS

    return recipes


def get_key(element, reactions):
    for key in reactions.keys():
        if key[1] == element:
            return key


def group_requirements(requirements):
    new_requirements = []
    for ele in requirements:
        exists = False
        for new_ele in new_requirements:
            if ele == new_ele:
                exists = True
                new_ele.quantity += ele.quantity
                break
        if (not exists):
            new_requirements.append(element(ele.get_tup()))
    return new_requirements


def update_requirements(required, reactions):
    new_required = []

    for ele in required:
        if ele.name == "ORE":
            new_required.append(ele)
            continue
        key = get_key(ele.name, reactions)
        while (key[0] < ele.quantity):
            new_required += [element(x) for x in reactions[key]]
            ele.quantity -= key[0]
        new_required += [element(x) for x in reactions[key]]

    return group_requirements(new_required)


def print_requirements(required):
    print("===========================")
    for ele in required:
        ele.show()
    print("===========================")
    return


if __name__ == "__main__":
    reactions = read_file(FILE_NAME)
    one_fuel = element((1, "FUEL"))
    required = [one_fuel]

    for _ in range(5):
        print_requirements(required)
        required = update_requirements(required, reactions)

    print_requirements(required)
