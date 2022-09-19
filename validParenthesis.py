class Solution:
    def isValid(self, s: str) -> bool:
        opened = 0
        closed = 0
        for index in range(len(s)):
            opened += int(s[index] == "(")
            closed += int(s[index] ==")")
            if closed > opened:
                return False 
        return opened == closed 
solution  = Solution()
s = input()
result = solution.isValid(s)
print(result)

                