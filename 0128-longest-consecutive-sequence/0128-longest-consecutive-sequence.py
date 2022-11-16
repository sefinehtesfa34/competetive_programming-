class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_values = set(nums)
        longest = 0
        visited = set()
        for num in nums:
            if num in visited:
                continue
            cur_length = 0
            while num in set_values:
                cur_length += 1
                visited.add(num)
                num += 1
            longest = max(longest, cur_length)
            
        return longest