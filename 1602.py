"""
Advent of Code 2019 - Day 16

Introduction

Author: Tom Kite
"""

from copy import deepcopy
from math import gcd

FILE_NAME = "1601.dat"
PATTERN = [0, 1, 0, -1]
STEPS = 100
INPUT_MULTIPLIER = 10000


def read_input(file_name):
    with open(file_name, 'r') as input_file:
        output = [int(x) for x in str(input_file.readline())]
    return output


def list_to_string(input_list):
    output = ""
    input_list = [str(x) for x in input_list]
    for x in input_list:
        output += x
    return output


def FFT_step(numbers, pattern, offset):
    output = [0]*len(numbers)
    output[-1] = numbers[-1]
    for i in range(len(output)-2, -1, -1):
        output[i] = output[i+1] + numbers[i]
    for i in range(len(output)):
        output[i] = output[i] % 10
    return output


def run_FFT(numbers, pattern, steps, offset, percentage_counter=False):
    for counter in range(steps):
        if (percentage_counter):
            print("{}% complete".format(100*counter/steps))
        numbers = FFT_step(numbers, pattern, offset)
    return numbers


if __name__ == "__main__":
    start_numbers = read_input(FILE_NAME)
    offset = int(list_to_string(start_numbers)[:7])

    desired_length = len(start_numbers) * INPUT_MULTIPLIER - offset
    numbers = start_numbers[offset % len(start_numbers):]
    numbers += start_numbers * ((desired_length-len(numbers))
                                // len(start_numbers))
    numbers += start_numbers[:len(numbers)-desired_length]

    print("\nRunning calculations")
    numbers = run_FFT(numbers, PATTERN, STEPS, offset, True)

    print("Starting numbers: %s...\nFinal numbers: ...%s...\nResult: %s"
          % (list_to_string(start_numbers)[:15],
             list_to_string(numbers)[:15],
             list_to_string(numbers)[:8]))
