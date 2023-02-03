class Solution:
    def validPalindrome(self, string: str) -> bool:
        def is_palindrome(left, right):
            while left < right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            return True
        left = 0
        right = len(string) - 1
        while left < right:
            if string[left] != string[right]:
                if is_palindrome(left, right - 1) or is_palindrome(left + 1, right):
                    return True
                return False
            left += 1
            right -= 1
        return True
            