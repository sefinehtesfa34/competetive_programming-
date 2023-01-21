class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0]*(len(s)+1) for _ in range(len(s) + 1)]  
        best_left = best_right = cur_answer = 0
        for index in range(len(s)):
            dp[index][index] = 1
        for step in range(1, len(s)):
            for left in range(len(s)-step):
                shift = step + left
                if s[shift] == s[left] and dp[left+1][shift-1] == shift - left - 1:
                    dp[left][shift] = 2 + dp[left + 1][shift - 1]
                if dp[left][shift] > cur_answer:
                    cur_answer = dp[left][shift]
                    best_left = left
                    best_right = shift
                    
        return s[best_left:best_right+1]
        