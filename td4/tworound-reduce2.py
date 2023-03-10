import sys


def calculate_value_from_list(reduce_list):
    i = 0
    result = 0
    while i < len(reduce_list) - 1:
        if reduce_list[i][0] == reduce_list[i + 1][0]:
            result += reduce_list[i][1] + reduce_list[i + 1][1]
            i += 2
        else:
            i += 1
    print(f"{prev_group[0]},{prev_group[1]}\t{str(result)}")



reduce_list = []
prev_group = None


for line in sys.stdin:

    i, k, value = line.strip().split('\t')

    value = int(value)
    group = (i,k)

    if group == prev_group:
        reduce_list.append((group, value))
    else:
        if prev_group:
            calculate_value_from_list(reduce_list)
        prev_group = group
        reduce_list = [(group, value)]


calculate_value_from_list(reduce_list)