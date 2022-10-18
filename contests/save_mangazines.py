from heapq import heapify, heappop
from typing import Counter


def getTest():
    return int(input())
def getNumBoxes():
    return int(input())
def getMagazines():
    return list(map(int, input().split()))
def getMaxMagazines(magazines, lids):
    bestSum = 0
    for index in range(len(lids)):
        if lids[index] == '1':
            bestSum += magazines[index]
    return updateBestSum(magazines, list(lids), bestSum)
# bestSum = max(bestSum, curSum), Update the previous sum if the current sum is greater than
# The previous sum
def updateBestSum(magazines, lids, bestSum):
    curSum = bestSum 
    for index in range(len(lids) - 1):
        if lids[index] == '0' and lids[index + 1] == '1':
            lids[index + 1] = '0'
            curSum += (magazines[index] - magazines[index + 1])
            bestSum = max(bestSum, curSum)
    return bestSum 

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