class Solution:
    def reverseWords(self, s: str) -> str:
        
        string = s.split()[::-1]
        return " ".join(string).strip()
        
    
        