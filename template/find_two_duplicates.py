class Solution:
    def duplicateii(self):
        
        n = int(input())
        nums = self.get_nums()
        x = y = xor = 0
        
        for index in range(1, n + 1):
            xor = xor ^ index
        
        for index in range(len(nums)):
            xor ^= nums[index]
        
        for index in range(1, n + 1):
            if index & (xor ^ -xor):
                x ^= index 
            else:
                y ^= index 
                
        for index in range(len(nums)):
            if nums[index]  & (xor & -xor):
                x ^= nums[index]
            else:
                y ^= nums[index]
            
            
        return print(x, y)
    
    def get_nums(self):
    
        return list(map(int, input().split()))
    
    
solution = Solution()
solution.duplicateii()
'''
8 4 2 1

0 1 0 0
0 0 1 1


'''