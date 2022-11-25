class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        contributions = defaultdict(lambda:[0, 0])
        def left_monotonic(nums):
            stack = []
            for index in range(len(nums) - 1, -1, -1):
                while stack and nums[stack[-1]] >= nums[index]:
                    cur_pos = stack.pop()
                    contributions[cur_pos][0] = cur_pos - index
                stack.append(index)
            for remain in stack:
                contributions[remain][0] = -stack[-1] + remain + 1
                
        def right_monotonic(nums):
            stack = []
            for index in range(len(nums)):
                while stack and nums[stack[-1]] > nums[index]:
                    cur_pos = stack.pop()
                    contributions[cur_pos][1] = index - cur_pos
                stack.append(index)
            
            for remain in stack:
                contributions[remain][1] = stack[-1] - remain + 1
        right_monotonic(arr)
        left_monotonic(arr)
        result = 0
        for index in contributions:
            result += arr[index] * contributions[index][0] * contributions[index][1]
            result %= (10 ** 9 + 7)
        return result % (10 ** 9 + 7)
        
        
        
        
        
        
        
        
        
        
        
            