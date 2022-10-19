class Solution:
    def subsetWithBits(self):
        nums = self.getNums()
        return self.generateSubsets(nums)
    
    def getNums(self):
        return list(map(int, input().split()))
    
    def generateSubsets(self, nums):
        n = len(nums)
        subsets = []
        for bit in range(1<<n):
            subset  = []
            for index in range(n):
                if bit & 1 << index:
                    subset.append(nums[index])
            subsets.append(list(subset))
        return subsets 
    
solution = Solution()
result = solution.subsetWithBits()
print(result)
'''
[1 2 3]
7
[111]
n = 3
32 16 8 4 2 1

            bit representation of the current number:                  n = 3
current = 0  000
current = 1  001
current = 2  010
current = 3  011
current = 4  100
current = 5  101
current = 6  110
current = 7  111
current  = 8
current = 9
current = 0
'''
