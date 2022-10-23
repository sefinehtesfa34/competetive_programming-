from functools import cache


class Solution:
    @cache
    def tripe_step(self, height):
        # if height == 0:
        #     return 1 
        # if height < 0:
        #     return 0
        # # I can move up with one step                             
        # one_step = self.tripe_step(height - 1)
        # # I can move up with two steps
        # two_step = self.tripe_step(height - 2)
        # # I can move up with three steps
        # three_step = self.tripe_step(height - 3)
        # return one_step + two_step + three_step 
        dp = [0]*(height + 1)
        dp[0] = 1
        for index in range(1, height + 1):
            dp[index] = dp[index - 1] + dp[index - 2] + dp[index - 3]
        return dp[index]
    
    
    
    '''
                                 5
                              /  |  \
                             4   3*   2*
                           / | \
                        3    2* 1*
                      / | \
                     2  1* 0
                   / | \        
                  1  0  -1
                  
    
    '''
solution = Solution()
height = int(input())
result = solution.tripe_step(height)
print(result)
        