from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.answer = []
        self.backtrack(n, n)
        return self.answer
    def backtrack(self, opened, closed, candidate = []):
        if closed < opened :
            return 
        if closed == 0 and opened == 0:
            self.answer.append("".join(candidate))
            return 
        
        if closed < 0 or opened < 0:
            return
        
        self.backtrack(opened - 1, closed,  candidate + ["("])
        self.backtrack(opened, closed - 1,  candidate + [')'])
        
        