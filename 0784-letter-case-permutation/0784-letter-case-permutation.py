from string import ascii_lowercase, ascii_uppercase
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        answer = []
        def backtrack(index, temp):
            if len(temp) == len(s):
                answer.append("".join(temp))
            if index == len(s):
                return 
            if s[index] in ascii_lowercase:
                backtrack(index + 1, temp + [ascii_uppercase[ord(s[index]) - ord('a')]])
            if s[index] in ascii_uppercase:
                backtrack(index + 1, temp + [ascii_lowercase[(ord(s[index])) - ord('A')]])
            backtrack(index + 1, temp + [s[index]])
                
        backtrack(0, [])
        return answer
    
                