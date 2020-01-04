"""
Advent of Code 2019 - Day 4

This program will look through a series of possible values, seeing if
they fit a series of rules

rule 3 is the difficult one added in the second version of the task

Author: Tom Kite
"""

start_val = 356261
finish_val = 846303

def count_letter(word, char):
    count = 0
    for c in word:
        if c == char:
            count += 1
    return count

def rule_1(string_num):
    for i in range(len(string_num)-1):
        if (string_num[i] == string_num[i+1]):
            return True
    return False

def rule_2(string_num):
    for i in range(len(string_num)-1):
        if (string_num[i] > string_num[i+1]):
            return False
    return True

def rule_3(string_num):
    for num in string_num:
        if (count_letter(string_num, num) == 2):
            return True
    return False


valid_inputs = []

for num in range(start_val,finish_val):
    string_form = str(num)
    if ( rule_1(string_form) and rule_2(string_form) and rule_3(string_form)):
        valid_inputs.append(string_form)

print(valid_inputs)

print ( len(valid_inputs) )