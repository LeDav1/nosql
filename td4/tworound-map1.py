#!/usr/bin/env python3

import sys

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    matrix_index, row, col, value = line.split('|')

    if matrix_index == "M": # (j,(M, i, mij ))
        print(f"{col}, {matrix_index}, {row}, {value}")
    else: # (i,(N, j, nij ))
        print(f"{row}, {matrix_index}, {col}, {value}")
