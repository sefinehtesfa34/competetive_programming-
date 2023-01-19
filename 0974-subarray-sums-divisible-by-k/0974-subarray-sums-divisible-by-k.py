class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hashmap = Counter()
        hashmap[0] = 1
        cur_sum = answer = 0
        for index in range(len(nums)):
            cur_sum += nums[index]
            mod = cur_sum % k
            answer += hashmap[mod]
            hashmap[mod] += 1
        return answer
    