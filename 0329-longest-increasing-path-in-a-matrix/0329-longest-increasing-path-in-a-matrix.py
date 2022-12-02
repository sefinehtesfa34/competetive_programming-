class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        indegree = Counter()
        dp = [[1]*len(matrix[0]) for _ in range(len(matrix))]
        graph = defaultdict(list)
        def is_bound(row, col):
            return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])
        
        def find_indegrees():
            for row in range(len(matrix)):
                for col in range(len(matrix[0])):
                    for dir in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
                        new_row = row + dir[0]
                        new_col = col + dir[1]
                        if is_bound(new_row, new_col):
                            if matrix[new_row][new_col] > matrix[row][col]:
                                indegree[new_row, new_col] += 1
                                graph[(row, col)].append((new_row, new_col))
                                
        def topoSort():
            result = 0
            queue = deque()
            for row in range(len(matrix)):
                for col in range(len(matrix[0])):
                    if indegree[row, col] == 0:
                        queue.append((row, col))
            while queue:
                row, col = queue.popleft()
                for child_row, child_col in graph[row, col]:
                    indegree[child_row, child_col] -= 1
                    if indegree[child_row, child_col] == 0:
                        queue.append((child_row, child_col))
                    dp[child_row][child_col] = max(dp[child_row][child_col], 1 + dp[row][col])
                    
            for row in range(len(dp)):
                for col in range(len(dp[0])):
                    result = max(result, dp[row][col])
            return result
        find_indegrees()
        return topoSort()
    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
            

        