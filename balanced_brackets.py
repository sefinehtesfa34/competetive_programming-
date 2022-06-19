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

def isBalanced(s):
    d={'(':')','{':'}','[':']'}
    l=[]
    for i in s:
        if i in d.keys():
            l.append(i)
        elif i in d.values():
            if len(l)==0:
                return 'NO'
            pop=l.pop()
            if d[pop]!=i:
                return 'NO'
    if len(l)==0:
        return 'YES'
    else:
        return 'NO'
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
