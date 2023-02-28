class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        n = len(matrix)
        m = len(matrix[0])
        dp = [0]*(m + 1)
        ans = 0
        for row in range(n):
            for col in range(m):
                dp[col] += 1
                if matrix[row][col] == '0':
                    dp[col] = 0
            stack = []
            for index in range(m + 1):
                while stack and (index == m or dp[stack[-1]] >= dp[index]): 
                    left = stack.pop()
                    right =  (index - left)
                    left_len = left - (stack[-1] if stack else -1)
                    right -= 1
                    ans = max(ans, min(left_len + right, dp[left])) 
                stack.append(index)
        return ans*ans
    