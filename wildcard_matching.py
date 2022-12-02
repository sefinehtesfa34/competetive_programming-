class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (1 + len(s)) for _ in range(len(p) + 1)]
        n = len(s)
        m = len(p)
        dp[0][0] = True
        for row in range(1, len(p) + 1):
            for col in range(1, len(s) + 1):
                if p[row - 1] == "*" and (p[row - 2] == s[col - 1] or p[row - 2] == "."):
                    dp[row][col] = dp[row -1][col] or dp[row][col - 1] or dp[row - 1][col - 1]
                elif p[row - 1] == '.' or p[row - 1] == s[col - 1]:
                    dp[row][col] =  dp[row - 1][col - 1]
                    
        return dp[m][n]
    '''
    [[] [a][a][b][c][b][b][b]
    [0, 0, 0, 0, 0, 0, 0, 0], [] 
    [0, 1, 1, 0, 0, 0, 0, 0], [a]
    [0, 1, 2, 0, 0, 0, 0, 0], [*]
    [0, 0, 0, 3, 0, 1, 1, 1], [b]
    [0, 0, 0, 1, 0, 1, 2, 3], [*]
    [0, 0, 0, 0, 2, 0, 0, 0], [c]
    [0, 0, 0, 0, 1, 0, 0, 0], [*]
    [0, 0, 0, 1, 0, 2, 1, 1], [b]
    [0, 0, 0, 1, 0, 1, 3, 4]  [*]
    ]
    
    [
    [] [a][a][b][c][b][b][b]
    [1, 0, 0, 0, 0, 0, 0, 0], [] 
    [0, 2, 0, 0, 0, 0, 0, 0], [a]
    [0, 1, 3, 0, 0, 0, 0, 0], [*]
    [0, 0, 0, 4, 0, 0, 0, 0], [b]
    [0, 0, 0, 1, 0, 1, 2, 3], [*]
    [0, 0, 0, 0, 2, 0, 0, 0], [c]
    [0, 0, 0, 0, 1, 0, 0, 0], [*]
    [0, 0, 0, 0, 0, 2, 0, 0], [b]
    [0, 0, 0, 1, 0, 1, 3, 4]  [*]
    ]
    '''
    
solution = Solution()
s = input()
p = input()
result = solution.isMatch(s, p)
print(result)