class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        def checker(left, right):
            palindrome = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                palindrome += 1
            return palindrome
        
        for index in range(len(s)):
            result += checker(index, index) + checker(index, index + 1)
        return result
    
    