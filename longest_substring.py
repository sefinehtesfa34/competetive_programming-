class Solution:
    def longestSubstringDigit(self, string):
        if not string:
            return 0
        leftPrefixSum = [0]*(len(string) + 1)
        rightPrefixSum = [0]*(len(string) + 1)
        n = len(string)
        for index, digit in enumerate(string, 1):
            leftPrefixSum[index] =  leftPrefixSum[index - 1] + int(digit)
            rightPrefixSum[n - index] = rightPrefixSum[n - index + 1] + int(string[n - index])
        
        def dp(left, right, longestSubstr):
            if left == right:
                return longestSubstr
            substr = string[left:right + 1]
            if len(substr) % 2 == 0:
                mid = len(substr)//2
                leftSum = leftPrefixSum[left + mid] - leftPrefixSum[left]
                rightSum = rightPrefixSum[left + mid] - rightPrefixSum[right]
                
                longestSubstr = len(substr) if (len(substr) > longestSubstr and leftSum == rightSum) else longestSubstr 
                print(substr, leftSum, rightSum)
            return max(dp(left + 1, right, longestSubstr), dp(left, right - 1, longestSubstr))
        return dp(0, n, 0)
        
solution = Solution()
string = input()
result = solution.longestSubstringDigit(string)
print(result)
        


'''
when the length is one and two: edge cases?

2 4 2 4



    dp(1424891) 
/         \
max(dp(424891), dp(142489))
/ \                     /  \  
max(dp(24891), dp(42489)) max(dp(42489), dp(14248))
                / \                            / \
            max(dp(2489), dp(4248))        max(dp(4248), dp(1424))
                            |                 | 
                            |                 |
                            |                 |

''' 

