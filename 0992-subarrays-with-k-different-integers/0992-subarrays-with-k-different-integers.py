class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmostK(nums, k):
            total_sub = left = 0
            hashmap = Counter()
            for index in range(len(nums)):
                hashmap[nums[index]] += 1
                while len(hashmap) > k:
                    hashmap[nums[left]] -= 1
                    if hashmap[nums[left]] == 0:
                        del hashmap[nums[left]]
                    left += 1
                total_sub += (index - left + 1)
            return total_sub
        return atmostK(nums, k) - atmostK(nums, k - 1)
    