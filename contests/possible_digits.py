class Solution:
    def solve(self):
        digits = self.get_digits()
        
        return self.possible_ways(digits)
    
    def possible_ways(self, digits, prev = -1000000, index = 0):
        if index == len(digits):
            return 1
        count = 0
        for cur in range(index, len(digits)):
            sub_digits = list(digits[index:cur + 1])
            sub_digits = list(map(int, sub_digits))
            sub_digits_sum = sum(sub_digits)
            if sub_digits_sum >= prev:
                count += self.possible_ways(digits, sub_digits_sum, cur + 1)
        return count 
    def get_digits(self):
        
        return input()
    
solution = Solution()
result = solution.solve()
print(result)
