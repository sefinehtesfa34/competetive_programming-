# Sum Swap: Given two arrays of integers, find a pair of values (one value from each array) that you 
# can swap to give the two arrays the same sum. 
# EXAMPLE 
# Input: {4, 2, 2, 1, 2} and {2, 6, 3, 3} 
# Output: {1, 3}
# Sum1 = 11 - 2 + 3 == 12
# sum2 = 14 - 3 == 11 + 2 == 13
# x + y = 4
# 15 - x + y == 11 - y + x
# 2y - 2x = -4
# 2x - 2y = 4
# x - y = 2
# 14 - y + x = 11 - x + y
# 2x - 2y = -1
# x - y = 0
# y - x = 0
# y = x
# 
class Solution:
    def swapSum(self, nums1, nums2):
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        if (sum2 - sum1) % 2:
            return []
        target = abs(sum1 - sum2)//2
        iterable = nums2 if sum2 <= sum1 else nums1
        visited = set(nums2) if sum2 >= sum1 else set(nums1) 
        pairs = [] 
        for num in iterable:
            if num + target in visited:
                pairs.append([target + num, num])
        return pairs
solution = Solution()
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
pairs = solution.swapSum(nums1, nums2)
print(pairs)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        











