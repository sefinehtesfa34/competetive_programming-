from math import ceil, log2


class Solution:
    def get_length(self):
        return int(input())
    def get_binary(self):
        return input()
    def random_test(self):
        self.get_length()
        binary = self.get_binary()
        decimal = self.binary_to_decimal(binary)
        return self.bitShift(decimal)
        
    def binary_to_decimal(self, binary):
        decimal = 0
        pointer = len(binary) - 1
        decimal = int(binary, 2)
        return decimal 
    def bitShift(self, decimal):
        bitSize = ceil(log2(decimal + 1))
        maxNum = 0
        for bit in range(bitSize):
            maxNum = max(maxNum, decimal | decimal >> bit)
        return maxNum 
solution = Solution()
result = solution.random_test()
print(bin(result)[2:])
            
                
                
                
        
        
        