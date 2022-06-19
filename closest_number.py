#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    arr.sort()
    l=[]
    mn=arr[1]-arr[0]
    for i,j in enumerate(arr):
        if i<len(arr)-1:
            if arr[i+1]-j<mn:
                mn=arr[i+1]-j
    for i in range(len(arr)-1):
        val=arr[i+1]-arr[i]
        if val==mn:
            l.extend([arr[i],arr[i+1]])
    return l
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
