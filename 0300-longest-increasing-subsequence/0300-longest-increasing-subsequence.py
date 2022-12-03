class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = []
        answer = 1
        for index in range(len(nums)):
            pos = bisect_left(stack, nums[index])
            if pos == len(stack) or not stack:
                stack.append(nums[index])
            else:
                stack[pos] = nums[index]
            answer = len(stack)
        return answer
            