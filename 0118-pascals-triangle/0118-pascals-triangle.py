class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        dp = [[1] for _ in range(numRows)]
        dp[0] = [1]
        dp[1] = [1, 1]
        for index in range(2, numRows):
            for curr in range(1, len(dp[index - 1])):
                dp[index].append(dp[index - 1][curr - 1] + dp[index - 1][curr])
            dp[index].append(1)
        return dp
    
        
        