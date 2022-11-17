class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        left = mid = inf
        for index in range(len(nums)):
            if nums[index] > mid:
                return True
            if nums[index] > left:
                mid = nums[index]
            else:
                left = nums[index]
        return False
        # 5 6 0 8