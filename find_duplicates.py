class Solution:
    def findDuplicates(self,nums):
        # Each element can be visited a maximum of two times: Time complexity = O(2N) = O(N)
        # Space complexity: O(1) Extra space.
        index = 0
        duplicated = set()
        while index < len(nums): # Time complexity: O(N)
            while nums[index] != index + 1:
                num = nums[index]
                if nums[index] == nums[num -  1]:
                    duplicated.add(num)
                    break
                nums[index], nums[num - 1] = nums[num - 1], nums[index] # Swap the two numbers
            index += 1
        return duplicated 
nums = list(map(int,input().split()))
solution = Solution()
result = solution.findDuplicates(nums)
print(result)
'''
duplicate = {2,3}
[0 1 2 3 4 5 0 0 0 0 0]

iterate : [ 2 2 3 4 5 3 1]
                        ^
'''