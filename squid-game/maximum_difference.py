class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        for index in range(len(nums)):
            for right in range(index + 1, len(nums)):
                if nums[index] != nums[right]:
                    ans = max(ans, nums[right] - nums[index])
        return ans
    