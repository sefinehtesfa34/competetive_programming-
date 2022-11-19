from collections import Counter

# from bisect import bisect_left 
# arr = [5,3,2,6,7,8]
# print(bisect_left(arr, 5))
class Solution:
    def letter_and_numbers(self):
        string = input()
        hashmap = Counter()
        let = num = longest = 0
        for index, char in enumerate(string):
            if char.isalpha():
                let += 1
            else:
                num += 1
            diff = let - num
            
            if let == num:
                longest = index  + 1
            
            if diff in hashmap:
                longest = max(longest, index - hashmap[diff])
            
            if diff not in hashmap:
                hashmap[diff] = index 
        
        return longest 
    
            
        
        
solution = Solution()
result = solution.letter_and_numbers()
print(result)

                
            
        