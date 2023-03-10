import sys

for line in sys.stdin:

    i, k, value = line.strip().split('\t')

    print(f"{i}\t{k}\t{value}")


