from itertools import accumulate
from typing import List


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        dp = [0]*1000_0001
        dp[grid[0][0] + 1] = 1
        for col in range(1, len(grid[0])):
            grid[0][col] = max(grid[0][col], grid[0][col - 1])
            dp[grid[0][col] + 1] += 1
            
        for row in range(1, len(grid)):
            grid[row][0] = max(grid[row][0], grid[row - 1][0])
            dp[grid[row][0] + 1] += 1
        for row in range(1, len(grid)):
            for col in range(1, len(grid[0])):
                grid[row][col] = max(grid[row][col], min(grid[row - 1][col], grid[row][col - 1]))
                dp[grid[row][col] + 1] += 1
        prefix = list(accumulate(dp, initial = 0))
        answer = []
        for query in queries:
            answer.append(prefix[query + 1])
        return answer 
solution = Solution()

grid = [[1,6,3],
        [2,5,7],
        [3,5,1]]

queries = [5,6,2]
result = solution.maxPoints(grid, queries)
print(result)
                
                
        