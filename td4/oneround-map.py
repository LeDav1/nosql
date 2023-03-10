import sys


len_m = 3
len_n = 4


for line in sys.stdin:

    matrix, row, col, value = line.strip().split('|')

    if matrix == "M":
	    for i in range(1,len_n + 1):
		    key = row + "," + str(i)
		    print("%s\t%s\t%s"%(key, col, value))
    else:
	    for j in range(1,len_m + 1):
		    key = str(j) + "," + col 
		    print("%s\t%s\t%s"%(key, row, value))


