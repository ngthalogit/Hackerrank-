#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks(h1, h2, h3):
    h1.reverse()
    h2.reverse()
    h3.reverse()
    h = 10000000
    
    l = [h1, h2, h3]
    for i in range(3):
        for j in range(len(l[i])):
            if j!=0:
                l[i][j] += l[i][j-1]
    while True:
        h = min(h, l[0][-1], l[1][-1], l[2][-1])
        for i in range(3):
            if l[i][-1] > h:
                l[i].pop()
        if len(l[0]) and len(l[1]) and len(l[2]):
            if l[0][-1]==l[1][-1] and l[0][-1]==l[2][-1]:
                return l[0][-1]
        else:
            return 0
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
