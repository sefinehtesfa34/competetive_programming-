class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        ans = 0
        for index in range(len(nums)):
            for next in range(index + 1, len(nums)):
                if (nums[index] + nums[next] == target):
                    ans += 1
                if nums[next] + nums[index] == target:
                    ans += 1
        return ans
    