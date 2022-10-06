from random import random


class Solution:
    def randomSet(self, array):
        if len(array) == 0:
            return []
        
        index = int(random() * (len(array) - 1))
        left = self.randomSet(array[:index])
        right = self.randomSet(array[index + 1:])
        return left + [array[index]] + right 
    [1,2,3,4]
    left = [1]
    right = [2, 3, 4]
    
        
        
        
solution = Solution()

array = list(map(int, input().split()))
result = solution.randomSet(array)
print(result)