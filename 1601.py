"""
Advent of Code 2019 - Day 16

Introduction

Author: Tom Kite
"""

import numpy as np
from copy import deepcopy

FILE_NAME = "1601.dat"
PATTERN = [0, 1, 0, -1]
STEPS = 100


def read_input(file_name):
    with open(file_name, 'r') as input_file:
        output = [int(x) for x in str(input_file.readline())]
    return output


def build_pattern(iterations, length, base_pattern):
    output = []
    for i in range(len(base_pattern)):
        for _ in range(iterations):
            output.append(base_pattern[i])
    output *= length // len(output) + 1
    return np.array(output[1:length+1])


def build_FFT_matrix(size):
    output = []
    for i in range(size):
        output.append(build_pattern(i+1, size, PATTERN))
    return output


def last_digit(numbers):
    for i in range(len(numbers)):
        numbers[i] = int(str(numbers[i])[-1])
    return numbers


def list_to_string(input_list):
    output = ""
    input_list = [str(x) for x in input_list]
    for x in input_list:
        output += x
    return output


if __name__ == "__main__":
    numbers = read_input(FILE_NAME)
    start_numbers = deepcopy(numbers)
    FFT_matrix = build_FFT_matrix(len(numbers))

    for _ in range(STEPS):
        numbers = np.dot(FFT_matrix, numbers)
        numbers = last_digit(numbers)

    print("Starting numbers: %s...\nFinal numbers: %s...\nResult: %s"
          % (list_to_string(start_numbers)[:15],
             list_to_string(numbers)[:15],
             list_to_string(numbers)[:8]))
