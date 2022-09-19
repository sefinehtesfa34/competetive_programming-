#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    val=arr[-1]
    for j in range(len(arr)-1,0,-1):
        if arr[j-1]<val:
            arr[j]=val
            for i in arr:
                print(i,end=" ")
            break
        elif j==1:
            arr[j]=arr[j-1]
            arr[j-1]=val
            for i in arr:
                print(i,end=" ")
            break
        arr[j]=arr[j-1]
        for i in arr:
            print(i,end=" ")
        print()
    
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
'''
k = 13
A = [1 2 4 7 11 45]
B = [2 9 11 12 22 23]


'''