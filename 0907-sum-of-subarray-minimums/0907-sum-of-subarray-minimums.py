class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        answer = 0
        n = len(arr)
        for index in range(n + 1):
            while stack and (index == n or arr[stack[-1]] > arr[index]):
                curr = stack.pop()
                left = curr - (stack[-1] if stack else -1)
                right = index - curr
                answer += arr[curr]*left*right
            stack.append(index)
        return answer % (1000_000_007)
        
        