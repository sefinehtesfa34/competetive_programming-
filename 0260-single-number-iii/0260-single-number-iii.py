class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = y = x = 0
        for num in nums:
            xor ^= num
        for num in nums:
            if num & (xor & -xor):
                x ^= num
            else:
                y ^= num
        return [x, y]
    