"""
Advent of Code 2019 - Day 8

Description

Author: Tom Kite
"""

import matplotlib.pyplot as plt
import numpy as np

file_name = "801.dat"
width = 25
height = 6
area = width*height


def read_data(file_name):
    with open(file_name) as input_file:
        data_string = [x for x in input_file.readline()]
    output_data = [int(x) for x in data_string]
    return output_data


if __name__ == "__main__":
    picture = read_data(file_name)

    number_of_layers = int(len(picture) / area)

    layers = []
    for i in range(number_of_layers):
        new_layer = picture[i*area:(i+1)*area]
        layers.append(new_layer)

    final_picture = [2]*area

    for pixel in range(area):
        temp_color = 2
        temp_delta = 0
        while (temp_color == 2):
            temp_color = picture[pixel + area*temp_delta]
            temp_delta += 1
        final_picture[pixel] = temp_color

    final_picture = np.reshape(final_picture, (height, width))

    print(final_picture)

    plt.imshow(final_picture)
