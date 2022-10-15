class Solution:
    def patternMatch(self, pattern, string):
        # preprocessing stage
        # pefix function or prefix table of fail function 
        F = [0]*(len(pattern))
        left = 0
        right = 1
        while right < len(F):
            if pattern[left] == pattern[right]:
                F[right] = left + 1
                left += 1
                right += 1
            elif left > 0:
                left = F[left - 1] 
            else:
                right += 1
        # Pattern matching stage
        ptr, strPtr = 0, 0
        while strPtr < len(string):
            if pattern[ptr] == string[strPtr]:
                ptr += 1
                strPtr += 1
            elif ptr > 0:
                ptr = F[ptr - 1]
            else:
                strPtr += 1
            if ptr == len(pattern):
                return True 
        return False 
solution = Solution()
pattern = input()
string = input()
result = solution.patternMatch(pattern, string)
print(result)