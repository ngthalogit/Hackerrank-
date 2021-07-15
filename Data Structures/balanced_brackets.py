#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(strings):
    loop = True
    stack = list()
    i = 0
    while i < len(strings) and loop:
        para = strings[i]
        if para in "{[(":
            stack.append(para)
        else:
            if len(stack)==0:
                return "NO"
            else:
                pop = stack.pop()
                opens = "{[("
                closes = "}])"
                if not (opens.index(pop) == closes.index(para)):
                    return "NO"
        i += 1
    if len(stack)==0:
        return "YES"
    else: return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
