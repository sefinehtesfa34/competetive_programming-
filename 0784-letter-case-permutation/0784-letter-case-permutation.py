from string import ascii_lowercase, ascii_uppercase
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        answer = []
        def backtrack(index, temp):
            if len(temp) == len(s):
                answer.append("".join(temp)) 
            if index == len(s):
                return 
            if s[index].isalpha():
                backtrack(index + 1, temp + [s[index].swapcase()])
            backtrack(index + 1, temp + [s[index]])
        backtrack(0, [])
        return answer
    
                