from collections import *
from math import *
class Solution:
    def is_bound(self, grid, row, col):
        
        return 0 <= row < len(grid) and 0 <= col < len(grid[0])

    def bfs(self, grid):
        queue = deque([(0, 0, 0)])
        dir = [(0, 1), 
               (1, 0), 
               (-1, 0), 
               (0, -1)
               ]
        n = len(grid)
        m = len(grid[0])
        cost = 0
        visited = set()
        while queue:
            row, col, cost = queue.popleft()
            if (row, col) == (n - 1, m - 1):
                return cost
            visited.add((row, col))
            for row_increase, col_increase in dir:
                new_row = row + row_increase
                new_col = col + col_increase
                if self.is_bound(grid, new_row, new_col) and (new_row, new_col) not in visited:
                    if grid[row][col] == grid[new_row][new_col]:
                        queue.appendleft((new_row, new_col, cost))
                    else:
                        queue.append((new_row, new_col, cost + 1))
        return cost


solution = Solution()
test = int(input())
for _ in range(test):
    grid = []
    n, m = list(map(int, input().split()))
    for _ in range(n):
        grid.append(input())
    result = solution.bfs(grid)
    print(result)
    





