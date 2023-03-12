#!/usr/bin/env python3
import sys

for line in sys.stdin:

    i, k, value = line.strip().split(' ')

    print(f"{i} {k} {value}")


