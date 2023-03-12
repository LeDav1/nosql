#!/usr/bin/env python3
import sys
import string

for line in sys.stdin:
    line = line.strip().lower()
    # remove punctuation and split into words
    words = line.translate(str.maketrans('', '', string.punctuation)).split()
    for word in words:
        print(f"{word}\t1")
