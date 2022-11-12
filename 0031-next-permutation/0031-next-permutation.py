
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_index = -1
        hashmap = {}
        for index in range(len(nums)):
            for curr in range(index + 1, len(nums)):
                if nums[index] < nums[curr]:
                    if index in hashmap:
                        hashmap[index] = curr if nums[curr] < nums[hashmap[index]] else hashmap[index]
                    else:
                        hashmap[index] = curr 
        for index in range(len(nums) - 1, -1, -1):
            if index in hashmap:
                nums[index], nums[hashmap[index]] = nums[hashmap[index]], nums[index] 
                last_index = index 
                break 
        nums[last_index + 1:] = sorted(nums[last_index + 1:])
        