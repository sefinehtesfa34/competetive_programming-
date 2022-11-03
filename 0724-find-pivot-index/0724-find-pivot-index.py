class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = list(accumulate(nums, initial = 0))
        for index in range(1, len(prefix)):
            if prefix[-1] - prefix[index] == prefix[index - 1]:
                return index - 1
        return -1
    