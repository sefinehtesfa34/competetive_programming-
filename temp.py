#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findDataLocations' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY locations
#  2. INTEGER_ARRAY movedFrom
#  3. INTEGER_ARRAY movedTo
#

def findDataLocations(locations, movedFrom, movedTo):
    hashmap = {}
    answer = []
    for move_from, move_to in zip(movedFrom, movedTo):
        hashmap[move_from] = move_to
    for val in locations:
        visited = set()
        while val in hashmap and val not in visited:
            visited.add(val)
            val = hashmap[val]
        answer.append(val)
    return sorted(answer)


            
        
        
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    locations_count = int(input().strip())

    locations = []

    for _ in range(locations_count):
        locations_item = int(input().strip())
        locations.append(locations_item)

    movedFrom_count = int(input().strip())

    movedFrom = []

    for _ in range(movedFrom_count):
        movedFrom_item = int(input().strip())
        movedFrom.append(movedFrom_item)

    movedTo_count = int(input().strip())

    movedTo = []

    for _ in range(movedTo_count):
        movedTo_item = int(input().strip())
        movedTo.append(movedTo_item)

    result = findDataLocations(locations, movedFrom, movedTo)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
