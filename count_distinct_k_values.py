class Solution:
    def countKDifference(self,k,nums):
        setValues = set(nums)
        counter = 0
        for num in nums:
            if num + k  in setValues:
                print(num, num + k)
                counter += 1
        return counter
solution = Solution()
nums = list(map(int,input().split()))
k = int(input())
result = solution.countKDifference(k, nums)
print(result)
