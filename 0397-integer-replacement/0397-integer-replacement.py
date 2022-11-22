class Solution:
    def integerReplacement(self, n: int) -> int:
        @cache
        def dp(cur_num):
            if cur_num == 1:
                return 0
            if cur_num % 2 == 0:
                return 1 + dp(cur_num // 2)
            return 2 + min(dp(cur_num // 2), dp(cur_num // 2 + 1))
        return dp(n)
    