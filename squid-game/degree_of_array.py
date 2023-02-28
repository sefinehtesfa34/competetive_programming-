from typing import List
from collections import Counter
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        n = len(nums)
        low = 1
        high = n + 1
        ans = max(Counter(nums).values())
        def check(window):
            hashmap = Counter()
            max_count = 0
            left = 0
            for index in range(n):
                hashmap[nums[index]] += 1
                max_count = max(max_count, hashmap[nums[index]])
                if index >= window - 1:
                    hashmap[nums[left]] -= 1
                    if hashmap[nums[left]] == 0:
                        del hashmap[nums[left]]
                    left += 1
            return max_count >= ans
        while low < high:
            mid = (low + high)>>1
            response = check(mid)
            if response == True:
                high = mid
            else:
                low = mid + 1
        return high
    
        
        