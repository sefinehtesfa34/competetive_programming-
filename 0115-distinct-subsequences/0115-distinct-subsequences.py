class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0]*(1 + len(t)) for _ in range(len(s) + 1)]
        for index in range(len(s)):
            dp[index][0] = 1
            
        for s1 in range(1, len(s) + 1):
            for t1 in range(1, len(t) + 1):
                take = dp[s1 - 1][t1 - 1] if s[s1 - 1] == t[t1 - 1] else 0
                dp[s1][t1] = dp[s1 - 1][t1] + take
                
        return dp[len(s)][len(t)]
    
        
        
#         @cache
#         def dp(s1, t1):
#             if t1 == len(t):
#                 return 1
#             if s1 == len(s):
#                 return 0
#             pick = 0
#             if s[s1] == t[t1]:
#                 pick =  dp(s1 + 1, t1 + 1)
#             not_pick = dp(s1 + 1, t1)
#             return pick + not_pick
#         return dp(0, 0)
    