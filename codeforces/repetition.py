from collections import Counter
class Solution:
    def repetition(self):
        
        string = input()
        if not string:
            return 0 
        longest = 1
        left = right = 0
        hashmap = Counter()
        prev = ''
        while right < len(string):
            hashmap[string[right]] += 1
            if string[right] != prev:
                left = right
                prev = string[right]
            longest = max(longest, right - left + 1)
            right += 1
        return longest         
solution = Solution()
result = solution.repetition()
print(result)
