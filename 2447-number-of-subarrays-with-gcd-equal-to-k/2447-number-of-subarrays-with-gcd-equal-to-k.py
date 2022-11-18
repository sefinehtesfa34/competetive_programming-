class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        answer = Counter(nums)[k]
        for index in range(len(nums)):
            cur_gcd = nums[index]
            for curr in range(index + 1, len(nums)):
                cur_gcd = gcd(cur_gcd, nums[curr])
                if cur_gcd == k:
                    answer += 1
        return answer
    
        
        