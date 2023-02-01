class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        ans = [[0]*(m) for _ in range(n)]
        prefix = [[0]*(m + 1) for _ in range(n + 1)]
        for row in range(1, n + 1):
            for col in range(1, m + 1):
                prefix[row][col] = mat[row - 1][col - 1] +\
                                   prefix[row - 1][col] +\
                                   prefix[row][col - 1] -\
                                   prefix[row - 1][col - 1]
        

        for row in range(n):
            for col in range(m):
                row1 = max(0, row-k)
                row2 = min(n, row + k + 1)
                col1 = max(0, col - k)
                col2 = min(m, col + k + 1)
                
                ans[row][col] = prefix[row2][col2] -\
                                        prefix[row2][col1] -\
                                        prefix[row1][col2] +\
                                        prefix[row1][col1]
        return ans
    
                                
        
        
        
        
        
        
        