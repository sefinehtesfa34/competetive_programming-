class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        table = [0]*(n + 1)
        left = 0
        right = 1
        while right < n:
            if needle[left] == needle[right]:
                left += 1
                table[right] = left
                right += 1
            elif left > 0:
                left = table[left - 1]
            else:
                right += 1
        strPtr = 0 #String pointer
        patternPtr = 0 # pattern pointer
        while strPtr < len(haystack):
            if patternPtr == len(needle):
                return strPtr - n
            if haystack[strPtr] == needle[patternPtr]:
                patternPtr += 1
                strPtr += 1
            elif patternPtr > 0:
                patternPtr = table[patternPtr - 1]
            else:
                strPtr += 1
        return -1 if patternPtr != n else strPtr - n
    
    
            
                
                
                
                
                
                
                
                
                
                
                
                