class Solution:
    def clearBitsThroughI(self, shift, num):
        mask = (1 << shift) - 1
        return num & mask
solution = Solution()
num, shift = list(map(int, input().split()))
result = solution.clearBitsThroughI(shift, num)
print(result)