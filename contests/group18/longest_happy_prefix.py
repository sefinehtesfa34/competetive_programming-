class Solution:
    def longestPrefix(self, s: str) -> str:
        
        prefix = [0]*len(s) 
        left = 0
        right = 1
        while right < len(s):
            if s[left] == s[right]:
                prefix[right] = left + 1
                left += 1
                right += 1
            elif left > 0:
                left = prefix[left - 1]
            else:
                right += 1
        return s[:prefix[-1]]
        
            