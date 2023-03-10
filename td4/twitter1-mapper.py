#!/usr/bin/env python
import sys

for line in sys.stdin:
    user, follower = line.strip().split(" ")

    print(f"{user} 1")