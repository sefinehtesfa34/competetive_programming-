class Solution:
    def pairSum(self,nums, target):
        sorted = [0]*(max(nums) + 1)
        pairs = []
        for num in nums:
            sorted[num] = num 
        for num in nums:
            find = target - num 
            if find < len(sorted) and sorted[find] != 0:
                pairs.append((num, find))
                sorted[num] = 0
        return pairs 
solution = Solution()
nums = list(map(int,input().split()))
target = int(input())
result = solution.pairSum(nums,target)
print(result)
