"""
Advent of Code 2019 - Day 12

Introduction

Author: Tom Kite
"""

from copy import deepcopy
from math import gcd


def grav_on_axis(A, B):
    if (A < B):
        return +1
    if (B < A):
        return -1
    return 0


class body:
    def __init__(self, in_x, in_y, in_z):
        self.x = in_x
        self.y = in_y
        self.z = in_z
        self.vx = 0
        self.vy = 0
        self.vz = 0
        return

    def __eq__(self, other):
        if (self.x != other.x or self.y != other.y or self.z != other.z):
            return False
        if (self.vx != other.vx or self.vy != other.vy or self.vz != other.vz):
            return False
        return True

    def eq_x(self, other):
        return (self.x == other.x and self.vx == other.vx)

    def eq_y(self, other):
        return (self.y == other.y and self.vy == other.vy)

    def eq_z(self, other):
        return (self.z == other.z and self.vz == other.vz)

    def get_energy(self):
        potential = abs(self.x) + abs(self.y) + abs(self.z)
        kinetic = abs(self.vx) + abs(self.vy) + abs(self.vz)
        return potential * kinetic

    def apply_velocity(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz
        return

    def gravity(self, other):
        self.vx += grav_on_axis(self.x, other.x)
        self.vy += grav_on_axis(self.y, other.y)
        self.vz += grav_on_axis(self.z, other.z)
        return

    def show(self):
        print("Position: (%i, %i, %i)\n Velocity: (%i, %i, %i)"
              % (self.x, self.y, self.z, self.vx, self.vy, self.vz))
        return


class system():
    def __init__(self, in_bodies):
        self.bodies = in_bodies

    def __eq__(self, other):
        for i in range(len(self.bodies)):
            if (self.bodies[i] != other.bodies[i]):
                return False
        return True

    def eq_x(self, other):
        for i in range(len(self.bodies)):
            if (not self.bodies[i].eq_x(other.bodies[i])):
                return False
        return True

    def eq_y(self, other):
        for i in range(len(self.bodies)):
            if (not self.bodies[i].eq_y(other.bodies[i])):
                return False
        return True

    def eq_z(self, other):
        for i in range(len(self.bodies)):
            if (not self.bodies[i].eq_z(other.bodies[i])):
                return False
        return True

    def apply_gravity(self):
        for i in range(len(self.bodies)):
            for j in range(len(self.bodies)):
                if (i != j):
                    self.bodies[i].gravity(self.bodies[j])
        return

    def apply_velocity(self):
        for body in self.bodies:
            body.apply_velocity()
        return

    def update_system(self):
        self.apply_gravity()
        self.apply_velocity()
        return

    def get_energy(self):
        total = 0
        for body in self.bodies:
            total += body.get_energy()
        return total


def lowest_common_multiple(numbers):
    lcm = numbers[0]
    for number in numbers[1:]:
        lcm = lcm * number // gcd(lcm, number)
    return lcm


"""
Coordinates are
<x=-13, y=14, z=-7>
<x=-18, y=9, z=0>
<x=0, y=-3, z=-3>
<x=-15, y=3, z=-13>
"""

if __name__ == "__main__":
    moons = []
    moons.append(body(-13, 14, -7))
    moons.append(body(-18, 9, 0))
    moons.append(body(0, -3, -3))
    moons.append(body(-15, 3, -13))

    moon_system = system(moons)
    original_moon_system = system(deepcopy(moons))

    moon_system.update_system()

    step_counter_x = 1
    step_counter_y = 1
    step_counter_z = 1

    x_found = False
    y_found = False
    z_found = False

    while (not x_found or not y_found or not z_found):
        if (not moon_system.eq_x(original_moon_system)):
            if (not x_found):
                step_counter_x += 1
        else:
            x_found = True

        if (not moon_system.eq_y(original_moon_system) and not y_found):
            if (not y_found):
                step_counter_y += 1
        else:
            y_found = True

        if (not moon_system.eq_z(original_moon_system) and not z_found):
            if (not z_found):
                step_counter_z += 1
        else:
            z_found = True

        moon_system.update_system()

    print("Steps taken for system to repeat: (%i,%i,%i)"
          % (step_counter_x, step_counter_y, step_counter_z))

    print("Lowest common multiple is: %i"
          % lowest_common_multiple((step_counter_x,
                                   step_counter_y,
                                   step_counter_z)))
