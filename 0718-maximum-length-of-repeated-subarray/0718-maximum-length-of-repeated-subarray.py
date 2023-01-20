class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0]*(len(nums2) + 1) for _ in range(len(nums1) + 1)]
        longest = 0
        for left in range(1, len(nums1) + 1):
            for right in range(1, len(nums2) + 1):
                if nums1[left - 1] == nums2[right - 1]:
                    dp[left][right] = 1 + dp[left - 1][right - 1]
                longest = max(longest, dp[left][right])
        return longest
    