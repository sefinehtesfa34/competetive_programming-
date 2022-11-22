class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        if k == 1:
            return sum(nums)
        
        low = max(nums)
        high = sum(nums)
        while low <= high:
            mid = (low + high) // 2
            count = 1 
            cur_sum = 0
            for num in nums:
                if cur_sum + num <= mid:
                    cur_sum += num
                else:
                    cur_sum = num
                    count += 1
            if count > k:
                low = mid + 1
            else:
                high = mid - 1
                
        return low