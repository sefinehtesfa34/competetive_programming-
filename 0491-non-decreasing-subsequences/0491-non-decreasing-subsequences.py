class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        dp = []
        for index in range(len(nums)):
            for left in range(len(dp)):
                if dp and dp[left][-1] <= nums[index]:
                    dp.append(dp[left] + [nums[index]])
            dp.append([nums[index]])
        answer = set()
        for sub in dp:
            if len(sub) > 1:
                answer.add(tuple(sub))
        return answer
                    