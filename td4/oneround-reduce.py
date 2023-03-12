#!/usr/bin/env python3
import sys


def calculate_value_from_list(value_list):
    i = 0
    result = 0
    while i < len(value_list) - 1:
        if value_list[i][0] == value_list[i + 1][0]:
            result += value_list[i][1]*value_list[i + 1][1]
            i += 2
        else:
            i += 1
    print(f"{prev_add_group}\t{str(result)}")


value_list = []
prev_add_group = None

for line in sys.stdin:
    add_group = []
    add_group1, add_group2, mul_group, value = line.rstrip().split(' ')
    add_group.append(add_group1)
    add_group.append(add_group2)
    #print(add_group, mul_group, value)
    mul_group, value = map(int, [mul_group, value])
    #print(mul_group, value)

    if add_group == prev_add_group:
        value_list.append((mul_group, value))
    else:
        if prev_add_group:
            calculate_value_from_list(value_list)
        prev_add_group = add_group
        value_list = [(mul_group, value)]


calculate_value_from_list(value_list)



