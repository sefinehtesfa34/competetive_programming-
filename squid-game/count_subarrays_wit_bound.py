class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        bad = max_index = min_index = -1
        ans = 0
        for index in range(len(nums)):
            if nums[index] == minK:
                min_index = index
            if nums[index] == maxK:
                max_index = index
            if minK > nums[index] or nums[index] > maxK:
                bad = index
            ans += max(0, min(min_index, max_index) - bad)
        return ans
        
        