#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(h):
    stack = []
    index = 0
    rs = 0
    while index < len(h):
        if len(stack) == 0 or h[stack[-1]] <= h[index]:
            stack.append(index)
            index += 1
        else:
            top = stack.pop()
            if len(stack)==0:
                s = h[top]*(index)
            else:
                s = h[top]*(index-stack[-1]-1)
            rs = max(rs, s)
    while len(stack):
        top = stack.pop()
        if len(stack)==0:
            s = h[top]*(index)
        else:
            s = h[top]*(index-stack[-1]-1)
        rs = max(rs, s)
    return rs
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
