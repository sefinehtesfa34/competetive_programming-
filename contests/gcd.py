class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        num1 = min(nums1)
        num2 = max(nums2)
        def recursive(num1, num2):
            if num1 == 0:
                return num2
            return recursive(num2 %num1, num1)
        return recursvie(num1, num2)
    
        
        