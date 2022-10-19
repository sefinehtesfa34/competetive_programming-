class Solution:
    def getNums(self):
        return list(map(int, input().split()))
    
    def subsets(self):
        nums = self.getNums()
        # Find all subsets of the given set
        return self.findSubsets(nums)
    # Generate all substes
    def findSubsets(self, nums, subsets = [], subset = [], index = 0):
        if index == len(nums):
            subsets.append(list(subset))
            return 
        self.findSubsets(nums, subsets, subset, index + 1)
        subset.append(nums[index])
        self.findSubsets(nums, subsets, subset, index + 1)
        subset.pop()
        return subsets
    
solution = Solution()
subsets = solution.subsets()
print(subsets)