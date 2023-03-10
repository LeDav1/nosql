#!/usr/bin/env python

import sys

# initialize variables
current_word = None
current_count = 0

# iterate over each line of input from stdin
for line in sys.stdin:
    # split key-value pair into word and count
    word, count = line.strip().split('\t')

    # convert count to integer
    count = int(count)

    # if the word has changed, output the current count and start a new count
    if current_word != word:
        if current_word:
            print(f"{current_word}\t{current_count}")
        current_word = word
        current_count = 0

    # add the count to the current count
    current_count += count

# output the final word count
if current_word:
    print(f"{current_word}\t{current_count}")

