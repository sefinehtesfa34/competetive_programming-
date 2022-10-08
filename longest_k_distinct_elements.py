from collections import Counter


class Solution:
    def solve(self, k, nums):
        left = longest = right = used = 0
        hashmap = Counter()
        for index in range(len(nums)):
            hashmap[nums[index]] += 1
            used += int(hashmap[nums[index]] == 1)
            while used > k:
                hashmap[nums[left]] -= 1
                if hashmap[nums[left]] == 0:
                    used -= 1
                left += 1
            longest = max(longest, index - left + 1)
        return longest

