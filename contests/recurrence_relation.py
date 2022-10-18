from functools import cache


class Solution:
    def topDownRecurrence(self, n):
        # T(1) = T(0) = 0
        # T(i) = 2*T(0) * T(1) + T(1) * 2*T(2) + T(3) + ....  2*T(n - 1) * T(n - 2)
        # The recurrence relation
        self.memo = [-1]*(n + 1)
        return self.recursive(n)
    def recursive(self, n):
        if self.memo[n] != -1:
            return self.memo[n]
        '''
        n = 3
        T(3) = 2 * T(0) * T(1) + 2 * T(1) * T(2) = 8 + 32 = 40
        T(2) = 2 * T(0) * T(1) = 8
        
        '''
        if n == 0 or n == 1: # The base case 
            return 2
        rightCall = self.recursive(n - 1) # The right subtree    
        leftCall = self.recursive(n - 2) #  The left subtree
        self.memo[n-1] = rightCall 
        self.memo[n-2] = leftCall 
        '''
        2 * dp(2) * dp(1) + 2 * dp(1) * dp(0) 
                            dp(2) = 8 
                            dp(3) = 2 * 8 * 2 = 32 + 8 = 40
        2 * dp(1) * dp(2) + dp(2)
                     |       |
                     8       2 * dp(0)*dp(1)
                            return 8
        '''          
        
        currentResult = 2 * leftCall * rightCall
        self.memo[n] = currentResult # The recurrence relation 
        return currentResult + self.recursive(n - 1) if n > 2 else currentResult 
    
    def bottomUp(self, n):
        dp = [0]*(n + 1) # Create a 1D array to store the computedd values started fromt the bottom.
        dp[0] = dp[1] = 2
        for index in range(2, n + 1): 
            dp[index] = 2*dp[index - 1] * dp[index - 2]  # The corresponding recurrence relation
            if index > 2:
                dp[index] += dp[index - 1]
        return dp[n]
solution = Solution()
num = int(input())
topDownResult = solution.topDownRecurrence(num)
bottomUpResult = solution.bottomUp(num)
print(topDownResult, bottomUpResult)

    
        
    
        