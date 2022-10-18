from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        for index in range(len(nums)):
            target = 0 - nums[index]
            hashmap = {}
            for cur in range(index + 1, len(nums)):
                if nums[cur] in hashmap:
                    result = tuple(sorted([nums[index], nums[cur], hashmap[nums[cur]]]))
                    answer.add(result)
                hashmap[target - nums[cur]] = nums[cur]
        return list(answer)
    
solution = Solution()
nums = list(map(int, input().split()))
result = solution.threeSum(nums)
print(result)
'''

nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
'''
            
