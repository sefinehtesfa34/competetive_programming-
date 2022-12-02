class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        contributions = defaultdict(lambda:[0, 0])
        def monotonic(nums, pos, start, end, step):
            stack = []
            for index in range(start, end, step):
                while stack and nums[stack[-1]] >= nums[index]:
                    if pos == 1 and nums[stack[-1]] == nums[index]:
                        break 
                    cur_pos = stack.pop()
                    contributions[cur_pos][pos] = abs(index - cur_pos)
                stack.append(index)
                
            for remain in stack:
                contributions[remain][pos] = abs(stack[-1] - remain) + 1
        monotonic(arr, 1, 0, len(arr), 1)
        monotonic(arr, 0, len(arr) - 1, -1, -1)
        result = 0
        for index in contributions:
            result += arr[index] * contributions[index][0] * contributions[index][1]
        return result % (10 ** 9 + 7)
    
    
    
    
    
    
    
    
    