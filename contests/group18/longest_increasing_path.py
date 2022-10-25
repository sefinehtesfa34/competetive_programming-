from typing import List
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        memo = {}
        def isBound(row, col):
            return 0 <= row and row <len(grid) and 0 <= col and col < len(grid[0])
        
        def dfs(row, col, visited = set()):
            if (row, col) in memo:
                return memo[(row, col)]
            
            if not isBound(row, col) or (row, col) in visited:
                return 0
            visited.add((row, col))
            
            count = 0
            for neighbor in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_row = row + neighbor[0]
                new_col = col + neighbor[1]            
                if isBound(new_row, new_col) and grid[new_row][new_col] > grid[row][col]:
                    count += dfs(new_row, new_col, visited)
            memo[(row, col)] =  1 + count
            
            return memo[(row, col)]
        
        current_count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                current_count += dfs(row, col)
        return current_count %(10**9+7)
    