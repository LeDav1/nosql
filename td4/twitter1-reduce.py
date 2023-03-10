#!/usr/bin/env python
import sys

prev_user = None
total_followers = 0

for line in sys.stdin:

    user, count = line.strip().split(" ")
    count = int(count)

    if user != prev_user:
        if prev_user:
            print(f"{prev_user}\t{total_followers}")
        prev_user = user
        total_followers = count
    else:
        total_followers += count

if prev_user:
    print(f"{prev_user}\t{total_followers}")

