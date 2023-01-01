class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        n = len(nums)
        for index in range(len(nums)):
            while stack and stack[-1] > nums[index] and len(stack) + n - index > k:
                stack.pop()
            stack.append(nums[index])
        while stack and len(stack) > k:
            stack.pop()
        return stack
    