from functools import cache
class Solution:
    def subsetSum(self, array, target):
        @cache
        def recursive(target, index):
            if target == 0:
                return True 
            if index == len(array) or target < 0:
                return False
            return recursive(target  - array[index], index + 1) or recursive(target, index + 1)
        return recursive(0, target)
    
solution = Solution()
target = int(input())
array = list(map(int, input().split()))
result = solution.subsetSum(array, target)
print(result)
dp = [[False]*(target + 1) for  _ in range(len(array) + 1)]
for index in range(len(array)):
    dp[index][0] = True 
for cur in range(1, len(array) + 1):
    for index in range(1, target + 1):
        if index >= array[cur - 1]:
            dp[cur][index] = dp[cur - 1][index - array[cur - 1]] or dp[cur - 1][index]
            
print(dp[len(array)][target])
'''
    [
    [True, False, False, True, False, False, False], 
    [True, False, True, True, False, True, False], 
    [True, True, True, True, True, True, True], 
    [True, False, False, False, False, False, True]
    ]

'''
        
'''

                            array = {3, 2, 1, 7}
                            target = 6
                            /           \ 
                        dp(3, 1)      dp(6, 1)
                     /        \         /    \ 
                dp(0, 2)  dp(3, 2)  dp(3, 2)  dp(6, 2)
                2 ** M
                where M is the height of the tree
                In worst case the height of the tree is len(array) = M.
                
                M = target
                Time complexity: O(2**M)
                Space complexity: O(M). This is because the recursion call stack.
                
                After memoization:
                Time complexity: O(M**2)
                Space complexity: O(M)
                
'''           