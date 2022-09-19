class Solution:
    def mergeSort(self,nums):
        if len(nums) <= 2:
            return sorted(nums) 
        '''
        nums = [7 3 9 6 4 5]
                    /  \
                [7 3 9]  [6 4 5]                    newArray = [3,4,5,6,7,9] => The sorted array                       
                /  \        / \                       [3,7,9]                [4,5,6]
              [7] [3 9]  [6] [4 5]                     /   \                /  \
                                              left =  [7]   right = [3, 9] [6]  [4 5]
                                                 newArray[3,7,9]
        '''                                                         
        mid = len(nums)//2
        leftNums = self.mergeSort(nums[:mid])
        rightNums = self.mergeSort(nums[mid:])
        left = 0
        right = 0
        newArray = []
        while left < len(leftNums) and right < len(rightNums):
            if leftNums[left] <= rightNums[right]:
                newArray.append(leftNums[left])
                left += 1
            else:
                newArray.append(rightNums[right])
                right += 1
        for index in range(left,len(leftNums)):
            newArray.append(leftNums[index])
        for index in range(right,len(rightNums)):
            newArray.append(rightNums[index])
        return newArray
solution = Solution()
nums = list(map(int,input().split()))
result = solution.mergeSort(nums)
print(result)
    
        
            
            
            
        
        
        
        