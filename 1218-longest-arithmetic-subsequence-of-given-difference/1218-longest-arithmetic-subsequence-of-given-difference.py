class Solution:
    def longestSubsequence(self, nums: List[int], difference: int) -> int:
        hashmap = Counter()
        for index in range(len(nums)):
            hashmap[nums[index]] = max(hashmap[nums[index]], 
                                       1 + hashmap[nums[index] - difference])
        return max(hashmap.values())
    