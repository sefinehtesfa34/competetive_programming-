class Solution:
    def rotated_array(self):
        nums = self.get_nums()
        target = self.get_target()
        
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid 
            
            if nums[mid] < nums[left]:
                if nums[mid] > target or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
                    
            else:
                if nums[mid] < target or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
    
    def get_nums(self):
        return list(map(int,input().split()))
    def get_target(self):
        return int(input())
    
solution = Solution()
result = solution.rotated_array()
print(result)