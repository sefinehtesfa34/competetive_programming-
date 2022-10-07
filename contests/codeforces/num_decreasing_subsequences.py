# class Solution:
#     def numberOfDecreasingSubsequen(self, nums):
#         indeces = self.longestSubsequence(nums)
#         newArray = []
#         for index in range(len(nums)):
#             if index in indeces:
#                 continue 
#             newArray.append(nums[index])
#         if len(newArray) == 0:
#             return 1
#         return 1 + self.numberOfDecreasingSubsequen(newArray)
    
#     def longestSubsequence(self, nums):
#         memo = {}
#         def dp(index, prev, longest, indeces = []):
#             if (index, prev) in memo:
#                 return memo[(index, prev)]
#             if index == len(nums):
#                 return (longest, indeces)
#             take = (0, [0])
#             if nums[index] < prev:
#                 take = dp(index + 1, nums[index], longest + 1, indeces + [index])
#             memo[(index,prev)] = max(take, dp(index + 1, prev, longest, indeces))
#             return memo[(index, prev)]
#         return dp(0, 1000000, 0)[1]
# nums = list(map(int, input().split()))
# solution = Solution()
# result = solution.numberOfDecreasingSubsequen(nums)
# print(result)

    
'''
2, 9, 12, 13, 4, 7, 6, 5, 10
[1,3,5,4,7]
'''
class Solution:
    def minimize(self, nums):
        subsequence = []
        def binarySearch(value):
            low = 0
            high = len(subsequence)
            while low < high:
                mid = (low + high)//2
                if subsequence[mid] <= value:
                    low = mid + 1
                else:
                    high = mid
            return low 
        for value in nums:
            index = binarySearch(value)
            if index == len(subsequence):
                subsequence.append(value)
            else:
                subsequence[index] = value 
        return len(subsequence)
solution = Solution()
nums = list(map(int, input().split()))
result = solution.minimize(nums)
print(result)
        
        
        
        