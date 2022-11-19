from collections import * 
class Solution:
    def contains_duplicate(self):
        # abs(nums[i] - nums[j]) <= valueDiff 
        # nums[i] > nums[j] - valueDiff
        # nums[i] <= valueDiff + nums[j]
        # nums[j] >= nums[i] - valueDiff
        #[1, 2, 4 , 1 ,6 , 6, 7]
        
        nums = self.get_nums()
        indexDiff, valueDiff = self.get_nums()
        
        diff_nums = self.get_diff(nums, valueDiff)
        add_nums = self.get_add(nums, valueDiff)
        
        maxs = self.max_window(add_nums, indexDiff)
        mins = self.min_window(diff_nums, indexDiff)
        if nums[0] > mins[indexDiff] or nums[0] <= maxs[indexDiff]:
            return True 
         
        for index in range(1,len(nums)):
            if index <= indexDiff:
                pointer = index - 1
                
            elif index + indexDiff >= len(nums):
                pointer = index + 1
            
            else:
                pointer  = index + indexDiff 
                     
            if pointer >= len(nums):
                return False 
            
            if nums[index] > mins[index - 1] or nums[index] > mins[pointer]\
            or nums[index] <= maxs[index - 1] or nums[index] <= maxs[pointer]:
                return print(True)
        return print(False)
           
    def get_diff(self, nums, value):
        for index in range(len(nums)):
            nums[index] -= value 
        return nums 
    
    def get_add(self, nums, value):
        for index in range(len(nums)):
            nums[index] += value 
        return nums   
        
    def max_window(self, nums, indexDiff):
        queue = deque()
        maxs = []
        for index in range(len(nums)):
            if queue and index - queue[0] >= indexDiff:
                queue.popleft()
                
            while queue and nums[queue[-1]] < nums[index]:
                queue.pop()
                
            queue.append(index)
            maxs.append(nums[queue[0]])
            
        last_index = index = len(nums)
        while queue:
            last_index = index = queue.popleft()
            maxs.append(nums[last_index])
        while last_index < len(nums):
            maxs.append(nums[index])
            last_index += 1
            
        return maxs
      
    
    
    def min_window(self, nums, indexDiff):
        queue = deque()
        mins = []
        for index in range(len(nums)):
            if queue and index - queue[0] >= indexDiff:
                queue.popleft()
                
            while queue and nums[queue[-1]] > nums[index]:
                queue.pop()
                
            queue.append(index)
            mins.append(nums[queue[0]])
            
        last_index = index = len(nums)
        while queue:
            last_index = index = queue.popleft()
            mins.append(nums[index])
        while last_index < len(nums):
            mins.append(nums[index])
            last_index += 1
        return mins 
    
    def get_nums(self):
        return list(map(int, input().split()))
        
solution = Solution()
result = solution.contains_duplicate()
print(result)
        
        
        
        