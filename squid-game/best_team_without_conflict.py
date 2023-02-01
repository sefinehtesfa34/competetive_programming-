class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores) 
        dp = [0]*(n + 1)
        pair = sorted(zip(ages, scores))
        for index in range(n):
            dp[index] = pair[index][1]
            for left in range(index):
                if pair[index][1] >= pair[left][1] or pair[index][0] == pair[left][0]:
                    dp[index] = max(dp[index] ,pair[index][1] + dp[left])
        return max(dp)
    
                    