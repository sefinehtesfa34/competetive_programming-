class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return 
        answer = []
        KEYS = ["", "", "abc", "def", "ghi",  "jkl",  "mno",  "pqrs", "tuv", "wxyz"]
        def backtrack(index, result):
            if index == len(digits):
                answer.append(result)
                return 
            strs = KEYS[int(digits[index])]
            for char in strs:
                backtrack(index + 1, result + char)
        backtrack(0, '')
        return answer
    
    
            
            