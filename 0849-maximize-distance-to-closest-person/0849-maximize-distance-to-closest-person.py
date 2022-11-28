class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_result = ones = 0
        stack = []
        dp = [0]*len(seats)
        for index in range(len(seats)):
            while stack and seats[stack[-1]] <  seats[index]:
                right = index - stack[-1]
                left = dp[stack.pop()]
                cur_min = min(left, right)
                max_result = max(max_result, cur_min)
            stack.append(index)
            ones += int(seats[index] == 1)
            dp[index] = (1 + dp[index - 1]) if seats[index] == 0 else 0
            max_result = max(max_result, dp[index]) if ones == 0 else max_result
            
        return max(dp[-1], max_result)
    