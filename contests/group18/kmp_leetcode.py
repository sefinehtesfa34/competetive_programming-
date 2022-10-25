class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # First we need to build a prefix suffix array. Check out KMP algorithm.
        # In short this means we need to store the length of subpattern 
        # that have the same prefix and suffix i.e pattern[:i] == pattern[-i:]
        # e.g leetcodeleet = pattern[:4] == pattern[-4:].
        # check the link for more information about KMP algorithm of pattern matching.
        # https://www.scaler.com/topics/data-structures/kmp-algorithm/
        table = self.prefixSuffixTable(needle)
        result = self.patternMatch(needle, haystack, table)
        return result
    # The table helps us to avoid backtracking when we didn't get a match for the pattern.
    # The link above helps you a lot if you didn't grasp the KMP algorithm.
    
    def prefixSuffixTable(self, pattern):
        table = [0]*(len(pattern))
        left = 0 
        right = 1
        while right < len(pattern): # Time complexity: O(m)
            if pattern[right] == pattern[left]:
                table[right] = left + 1
                left += 1
                right += 1
            elif left > 0:
                left = table[left - 1]
            else:
                right += 1
        return table
    # Pattern match.
    #Space complexity: O(m)
    #Time complexity: O(n + m)
    def patternMatch(self, pattern, string, table):
        patternPtr = 0
        strPtr = 0
        while strPtr < len(string): # Time complexity: O(n + m)
            if string[strPtr] == pattern[patternPtr]:
                patternPtr += 1
                strPtr += 1
            elif patternPtr > 0:
                patternPtr = table[patternPtr - 1]
            else:
                strPtr += 1
            if patternPtr == len(pattern):
                return strPtr - len(pattern)
        return  -1
            
            
                
            
        
        