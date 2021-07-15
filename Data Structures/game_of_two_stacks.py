#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER maxSum
#  2. INTEGER_ARRAY a
#  3. INTEGER_ARRAY b
#

def twoStacks(maxSum, a, b):
    rnns, i, j = 0, 0, 0
    for v in a:
        if rnns + v <= maxSum:
            rnns += v
            i += 1
        else: break
    ans = i
    while j < len(b) and i > -1:
        rnns += b[j]
        j += 1
        while rnns > maxSum and i > -1:
            i -= 1
            rnns -= a[i]
        if rnns <= maxSum and i+j > ans:
            ans = i+j        
    return ans
                    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        maxSum = int(first_multiple_input[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(maxSum, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()


