class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def dp(s1, t1):
            if t1 == len(t):
                return 1
            if s1 == len(s):
                return 0
            pick = 0
            if s[s1] == t[t1]:
                pick =  dp(s1 + 1, t1 + 1)
            not_pick = dp(s1 + 1, t1)
            return pick + not_pick
        return dp(0, 0)
    