class Solution:
    def numberOfWays(self, s: str) -> int:
        ones = zeros = r_ones = r_zeros = 0
        ans = 0
        n = len(s)
        for index in range(n-1, -1, -1):
            ones += s[index] == '1'
            zeros += s[index] == '0'
            if s[index] == '0':
                r_ones += ones
                ans += r_zeros
            if s[index] == '1':
                r_zeros += zeros
                ans += r_ones
                
        return ans
    