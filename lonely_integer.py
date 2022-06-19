#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    dictionary={}
    for i in range(len(a)):
        if a[i] not in dictionary:
            dictionary[a[i]]=1
        else:
            dictionary[a[i]]+=1
    listVal=list(dictionary.values())
    listKey=list(dictionary.keys())
    index_of_min=listVal.index(1)
    return listKey[index_of_min]
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
