#!/bin/python3

import math
import os
import random
import re
import sys

def matchingStrings(strings, queries):
    list1=[]
    for i in queries:
        count=0
        for j in strings:
            if i==j:
                count+=1
        list1.append(count)
    return list1
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
