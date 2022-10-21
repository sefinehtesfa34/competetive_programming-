class Solution:
    def longest_increasing_subsequence(self):
        nums = self.get_nums()
        longest = [1]*(len(nums))
        #[1, 2, 3, 4]
        # longest[2] = 2
        #longest[1] = 1
        #longest[3] = max(longest[2] + 1, longest[1] + 1)
        #longest[4] = max(longest[3] + 1, longest[2] + 1, longest[1] + 1) 
        #longest[4] = 1 + max(longest[3], longest[2], longest[1])
        #
        for index in range(len(nums)):
            for current in range(index):
                if nums[current] < nums[index]:
                    longest[index] = max(longest[index], 1 + longest[current])
            
        return print(max(longest))
    
    def get_nums(self):
        return list(map(int, input().split()))
    
    
    
solution = Solution()
solution.longest_increasing_subsequence()
