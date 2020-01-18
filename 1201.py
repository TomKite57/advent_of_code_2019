"""
Advent of Code 2019 - Day 12

Introduction

Author: Tom Kite
"""


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


def apply_all_grav(body_list):
    for i in range(len(body_list)):
        for j in range(len(body_list)):
            if (i != j):
                body_list[i].gravity(body_list[j])
    return


def apply_all_velocity(body_list):
    for body in body_list:
        body.apply_velocity()
    return


def get_total_energy(body_list):
    total = 0
    for body in body_list:
        total += body.get_energy()
    return total


"""
Coordinates are
<x=-13, y=14, z=-7>
<x=-18, y=9, z=0>
<x=0, y=-3, z=-3>
<x=-15, y=3, z=-13>
"""

if __name__ == "__main__":
    TOTAL_STEPS = 1000

    moons = []
    moons.append(body(-13, 14, -7))
    moons.append(body(-18, 9, 0))
    moons.append(body(0, -3, -3))
    moons.append(body(-15, 3, -13))

    for _ in range(TOTAL_STEPS):
        apply_all_grav(moons)
        apply_all_velocity(moons)

    print("Total energy in system after %i steps is %i"
          % (TOTAL_STEPS, get_total_energy(moons)))
