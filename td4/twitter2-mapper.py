#!/usr/bin/env python3
import sys

for line in sys.stdin:

    user, follower = line.strip().split('\t')

    print(f"{user}\t{follower}")


