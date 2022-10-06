'''
17.5 Letters and Numbers; Given an array filled with letters and numbers, 
find the longest subarray with 
an equal number of letters and numbers. 

'''

class Solution:
    def longestSubarray(self, array):
        hashmap  = {}
        letterCount = numberCount = longest = 0 
        for index in range(len(array)):
            letterCount += int(array[index].isalpha())
            numberCount += int(not array[index].isalpha())
            diff = letterCount - numberCount 
            if diff not in hashmap:
                hashmap[diff] = index 
            else:
                longest = max(longest, index - hashmap[diff])
        return longest 
    
        
        
solution = Solution()
array = input()
result = solution.longestSubarray(array)
print(result)
