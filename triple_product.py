from cmath import inf
class Solution:
    def tripleProduct(self,nums):
        nums.sort()
        positive  =nums[-3] * nums[-1] * nums[-2]
        negative_and_positive = nums[0] * nums[1] * nums[2]
        return max(positive,negative_and_positive)
solution = Solution()
nums = list(map(int, input().split()))
output = solution.tripleProduct(nums)
print(output)