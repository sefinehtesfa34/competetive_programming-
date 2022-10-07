'''
There are some processes that need to be executed. The amount of load that process causes a server that runs it, is being represented by a single integer. The total load caused on a server is the sum of the loads of all the processes that run on that server. You have at your disposal two servers, on which the mentioned processes can be run. Your goal is to distribute given processes between those two servers in a way that, the absolute difference of their loads will be minimized. 
Given an array of A[] of N integers, which represents loads caused by successive processes, the task is to print the minimum absolute difference of server loads. 
Examples:

Input: A[] = {1, 2, 3, 4, 5} 
Output: 1 
Explanation: 
Distribute the processes with loads {1, 2, 4} on the first server and {3, 5} on the second server, so that their total loads will be 7 and 8, respectively. 
The difference of their loads will be equal to 1.

Input: A[] = {10, 10, 9, 9, 2} 
Output: 0

'''
# I have two servers, so I can distribute those loads into the two servers
# The task is minimize their absolute difference
# Approach:
# Find the total sum of the loads and divide that in half
# No I have the capacity of the two servers
# Then maximize the number of loads for each capacity and all the loads in the two servers
# should be distinct (their position in the loads)
from cmath import inf
class Solution:
    def minAbsDiff(self, loads):
        totalLoad = sum(loads)
        halfCap = totalLoad // 2
        memo = {}
        minDiff = inf
        def findMax(cap, index):
            if (cap, index) in memo:
                return memo[(cap, index)]
            if index == len(loads) or cap < loads[index] :
                return 0
            memo[(cap, index)] = max(loads[index] + findMax(cap - loads[index], index + 1),findMax(cap, index + 1))
            return memo[(cap, index)]
        for index in range(len(loads)):
            minDiff = min(minDiff, abs(totalLoad - 2 * findMax(halfCap, index)))
        
        return minDiff
    
solution = Solution()
loads = list(map(int, input().split()))
result = solution.minAbsDiff(loads)
print(result)


totalLoad = sum(loads)
halfCap = totalLoad // 2
dp = [[0]*(halfCap + 1) for _ in range(len(loads) + 1)]
for index in range(1, len(loads) + 1):
    for cap in range(1, halfCap):
        value = loads[index - 1]    
        if value < cap:
            dp[index][cap] = max(value + dp[index][cap - value], dp[index - 1][cap])
        else:
            dp[index][cap] = dp[index - 1][cap]
print(dp[index][cap])

'''

'''




