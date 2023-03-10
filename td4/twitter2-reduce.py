#!/usr/bin/env python3
import sys

nb_user = 0
sum = 0

min_user = None
min_followers = 0

max_user = None
max_followers = 0


for line in sys.stdin:

    user, count = line.strip().split("\t")
    count = int(count)

    nb_user += 1
    sum += count
     
    if count < min_followers or min_user is None:
        min_user = user
        min_followers = count

    if count > max_followers or max_user is None:
        max_user = user
        max_followers = count


print(f"nb_users\t {nb_user}")
print(f"sum\t {sum}")
print(f"min\t {min_followers};{min_user}")
print(f"max\t {max_followers};{max_user}")
    