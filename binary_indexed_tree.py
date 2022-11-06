class Solution:
    def binary_indexed(self):
        nums = self.get_nums()
        data = [0]*(len(nums) + 1)
        for index in range(len(nums)):
            self.update(data, index, nums[index])
        return print(self.get_sum(data, 5))
        
    def get_nums(self):
        return list(map(int, input().split()))
        
    def get_parent(self, bit):
        return bit - (bit & -bit)
    def get_next(self, bit):
        return bit + (bit & -bit)
    def get_sum(self, data, index):
        index += 1
        cur_sum = 0
        while index > 0:
            cur_sum += data[index]
            index = self.get_parent(index)
        return cur_sum 
    def update(self, data, index, value):
        index += 1
        while index < len(data):
            
            data[index] += value 
            index = self.get_next(index)
        
            
solution = Solution()
solution.binary_indexed()
