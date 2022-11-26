class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @cache
        def dp(index, current):
            if index == len(triangle):
                return 0
            return triangle[index][current] + min(dp(index + 1, current + 1), dp(index + 1, current))
        return dp(0, 0)
    