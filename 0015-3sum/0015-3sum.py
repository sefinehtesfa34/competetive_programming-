class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        for index in range(len(nums)):
            target = 0 - nums[index]
            hashmap = {}
            for cur in range(index + 1, len(nums)):
                if nums[cur] in hashmap:
                    result = tuple(sorted([nums[index], nums[cur], hashmap[nums[cur]]]))
                    answer.add(result)
                hashmap[target - nums[cur]] = nums[cur]
        return list(answer)