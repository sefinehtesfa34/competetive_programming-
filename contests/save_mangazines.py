from cmath import inf
from heapq import heapify, heappop
from typing import Counter


def getTest():
    return int(input())
def getNumBoxes():
    return int(input())
def getMagazines():
    return list(map(int, input().split()))
def getMaxMagazines(magazines, lids):
    curMin = inf
    curSum = 0
    index = 0
    result = 0
    while index < len(lids):
        while index < len(lids) and lids[index] == '1':
            curSum += magazines[index]            
            curMin = min(curMin, magazines[index])
            index += 1
        if index == len(lids):
            break 
        print(curSum)
        result += max(0, curSum - curMin)
        curSum = magazines[index]
        curMin = magazines[index]
        index += 1

    return result 
        
            
    

def getLids():
    return input() 
def main():
    test = getTest()
    for _ in range(test):
        numMBoxes = getNumBoxes()
        lids = getLids()
        magazines = getMagazines()
        print(getMaxMagazines(magazines, lids))
main()