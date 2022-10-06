class Solution:
    def quickSort(self, nums):
        def quickSort(left, right):
            low = left 
            high = right 
            if left >= right:
                return
            mid = (left + right)//2
            pivot = nums[mid]
            while left <= right:
                while nums[left] < pivot:
                    left += 1
                while nums[right] > pivot:
                    right -= 1
                if left <= right:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right -= 1
            quickSort(low, left - 1)
            quickSort(left, high)    
        quickSort(0, len(nums) - 1)
        return nums 
    
                
            
        
        
        
        
        
solution = Solution()
nums = list(map(int, input().split()))
result = solution.quickSort(nums)
print(result)
 
    