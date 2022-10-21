from math import floor, log2


class Solution:
    def range_minimum(self):
        queries = self.get_queries()
        nums = self.get_array()
        table = self.min_precalculator(nums) # Create a min precalculator for a power of 2 length subarrays
        for query in queries:
            left_index, right_index = query[0], query[1]
            current_min = self.min_query(left_index, right_index, table) # return the current min in the given range
            print(current_min)
    
    def get_queries(self):
        n = int(input())
        queries = []
        for _ in range(n):
            queries.append(list(map(int, input().split())))
        return queries 
    
    def get_array(self):
        return list(map(int, input().split()))
    
    def min_query(self, left_index, right_index, table):
         
        nearest_power_of_two = 2**floor(log2(right_index - left_index + 1))
        cur_left, cur_right = left_index, left_index + (nearest_power_of_two - 1)
        cur_right_left, cur_right_right = right_index - (nearest_power_of_two - 1), right_index
        
        return min(table[(cur_right_left, cur_right_right)], table[(cur_left, cur_right)])
               
    def min_precalculator(self, nums):
        index = 0
        table  = {}
        while 2**index < len(nums):
            left = 0
            right = 2**index - 1
            while right < len(nums):
                table[(left, right)] = min(nums[left:right + 1])
                right += 1
                left += 1
            index += 1
        return table 
solution = Solution()
solution.range_minimum()

    
        
        
