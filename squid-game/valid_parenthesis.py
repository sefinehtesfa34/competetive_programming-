class Solution:
    def checkValidString(self, s: str) -> bool:
        @cache
        def dp(index, opened):
            if opened < 0:
                return False
            if index == len(s):
                return opened == 0
            
            add = sub = possible = skip = False
            if s[index] == '(':
                add = dp(index + 1, opened + 1)
            if s[index] == ')':
                sub = dp(index + 1, opened - 1)
            if s[index] == '*':
                possible = dp(index + 1, opened - 1) or dp(index + 1, opened + 1)
                skip = dp(index + 1, opened)
            return add or sub or possible or skip
        return dp(0, 0)
        