class Solution:
    def longest_palindrome_substring(self):
        string = input()
        dp = [[False] * (len(string)) for _ in range(len(string))]
        longest = [0, 1]
        for index in range(len(string)):
            dp[index][index] = True 
            
        for steps in range(1, len(string)):
            for curr_index in range(len(string) - steps):
                right = curr_index + steps 
                left = curr_index 
                if steps == 1:
                    dp[left][right] = string[right] == string[left] 
                else:
                    dp[left][right] = string[left]== string[right]  and dp[left + 1][right - 1]
                if dp[left][right]:
                    longest = [left, right + 1]
                    
        return print(*string[longest[0]:longest[1]])
    
                
solution = Solution()
solution.longest_palindrome_substring()

                