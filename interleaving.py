class Solution:
    def isInterleaving(self, str1, str2, finalStr):
        
        def recursive(str1ptr, str2ptr, finalPtr):
            if str1ptr == len(str1) and str2ptr == len(str2) and finalPtr == len(finalStr):
                return True 
            if finalPtr == len(finalStr):
                return False 
            if str1ptr < len(str1) and str1[str1ptr] == finalStr[finalPtr]:
                if recursive(str1ptr + 1, str2ptr, finalPtr + 1):
                    return True 
            elif str2ptr < len(str2) and str2[str2ptr] == finalStr[finalPtr]:
                if recursive(str1ptr, str2ptr + 1, finalPtr + 1):
                    return True 
            return False 
        return recursive(0, 0, 0)
solution = Solution()
str1 = input()
str2 = input()
finalStr = input()
result = solution.isInterleaving(str1, str2, finalStr)
print(result)
'''
dp = [[False] * (len(str2) + 1) for _ in range(len(str1) + 1)]
interleave = adebbf

    [] [d] [e] [f]
[]   T  F   F   F
[a]  T  T   
[b]  T
[b]  F

adabc
^
abc
^
ad
^


str1ptr = str2ptr = interleaveptr = 0
while str1ptr != len(str1) or str2ptr != len(str2):
    if str1[str1ptr] == interleave[interleaveptr] and str2[str2ptr] != interleave[interleaveptr]:
        str1ptr += 1
        interleaveptr += 1
    if str2[str2ptr] == interleave[interleaveptr] and str1[str1ptr] != interleave[interleaveptr]:
        str2ptr  += 1
        interleaveptr += 1
     










                                         
                                            finalStr  size = 1
                                         /            \
                        dp(str1 + 1, str2\, finalStr + 1)    dp(str1, str2 + 1, finalStr + 1) size = 2
                        /                           \
        dp(str1 + 1, str2, finalStr + 1)      dp(str1, str2 + 1, finalStr + 1) size = 4
         /                         \
dp(str1 + 1, str2, finalStr + 1)    dp(str1, str2 + 1, finalStr + 1) size = 8
                                                    a = bba
                                                    b = dabba
                                                    dbbaabba
                                                    dp(abbac, abba, abbbaabbac)
                                                                              \
                                                                        dp(bba, abba, bbaabba)
                                                                        /
                                                                    dp(ba, abba, baabba)
                                                                    /
                                                                dp(a, abba, aabba)
                                                                /
                                                            dp('', abba, abba)
                                                                        \
                                                                    dp('', bba, bba)
                                                                          \
                                                                    dp('', ba, ba)
                                                                            \
                                                                    dp('', a, a)
                                                                              \
                                                                    dp('', '', '')
                                                                    
                                                                        
                                                                             
                                                            
                                                
                                                    


.
.
.

size = 2 ** n where n is the height of the tree


So,
Time complexity: O(2**N) where N is the maximum length of str1 and str2; N = max(n, m) n = len(str1), m = len(str2)
space complexity: O(N)







'''



