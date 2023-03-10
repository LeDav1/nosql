#!/usr/bin/env python3

import sys
# We hate magic numbers
MATRIX_NAME = 0
I_OR_K = 1
VALUE = 2

reduce_list = []    # List of (matrix_name, i_or_k, value) tuples with the same j
previous_j = None
previous_matrix_index = None
previous_i_or_k = None
previous_value = None

for line in sys.stdin:
    
    j ,matrix_index, i_or_k, value = line.rstrip().split(", ") # j, (M, i, mij) or (N, k, nkj) as stated in mmds

    if j == previous_j or not previous_j:                   # If j is the same as previous j
        reduce_list.append((matrix_index, i_or_k, value))   # Form a new sublist, which is a group of lines sharing the same j
    else:                                                   # End of a group, For each key j, examine its list of associated values and print (i, k, mij * nki)
        delta = 1                                           # delta is the index of the next line (matrix_name, i_or_k, value) in the list
        while reduce_list:
            if delta < len(reduce_list):
                if reduce_list[0][MATRIX_NAME] != reduce_list[delta][MATRIX_NAME]:      # If the matrix_name is different, print the combination
                    print(f"{reduce_list[0][I_OR_K]}\t{reduce_list[delta][I_OR_K]}\t{int(reduce_list[0][VALUE]) * int(reduce_list[delta][VALUE])}")
                delta += 1
            else: 
                reduce_list.pop(0)                      # Remove the first element in the list, for which we have already printed all the possible combinations
                delta = 1                               # Reset delta to 1 for the next M 
        reduce_list = [(matrix_index, i_or_k, value)]   # Form a new sublist (matrix_index, i_or_k, value)
            
    previous_j = j
    previous_matrix_index = matrix_index
    previous_i_or_k = i_or_k
    previous_value = value

# We have to print the last group of j
delta = 1
while reduce_list:
    if delta < len(reduce_list):
        if reduce_list[0][MATRIX_NAME] != reduce_list[delta][MATRIX_NAME]:
            print(f"{reduce_list[0][I_OR_K]}\t{reduce_list[delta][I_OR_K]}\t{int(reduce_list[0][VALUE]) * int(reduce_list[delta][VALUE])}")
        delta += 1
    else: 
        reduce_list.pop(0)
        delta = 1
reduce_list = [(matrix_index, i_or_k, value)]   # Form a new sublist (matrix_index, i_or_k, value)
