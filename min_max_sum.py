#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    
    
    mx=max(arr)
    index=arr.index(mx)
    val=arr.pop(index)
    print(sum(arr),end=" ")
    arr.append(val)
    mn=min(arr)
    index=arr.index(mn)
    arr.pop(index)
    sm1=sum(arr)
    print(sm1)
    
            
        
    # Write your code here

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
