class Solution:
    def permutations(self):
        nums = self.getNums()
        return self.generatePermutations(nums)
    def getNums(self):
        return list(map(int, input().split()))
    def generatePermutations(self, nums, index = 0, currentPermutation =[], permutations = [], chosen = []):
        if len(currentPermutation) == len(nums):
            permutations.append(list(currentPermutation)) # One of the valid permutation
            return 
        for index in range(len(nums)):
            if index >= len(chosen):
                chosen.append(True)
            if chosen[index] == True:
                chosen[index] = False 
                currentPermutation.append(nums[index])
                self.generatePermutations(nums, index + 1, currentPermutation, permutations, chosen)
                currentPermutation.pop()
                chosen[index] = True 
        return permutations 
solution = Solution()
result = solution.permutations()
print(result)

            
        
        