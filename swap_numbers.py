from math import ceil, log2


class Solution:
    def swap(self,num1,num2):
        bitSize = ceil(log2(max(num1,num2) + 1))
        for bit in range(bitSize):
            mask = ~(1 << bit)
            num1 = (num1 & mask) | int(num2 & 1 << bit != 0) << bit   
            num2 = (num2 & mask) | int(num1 & 1 << bit != 0) << bit 
            
        return num1,num2  
solution = Solution()
num1 = int(input())
num2 = int(input())
print("Before: ","num1 = ",num1,"num2 = ",num2)
num1, num2 = solution.swap(num1,num2)
print("After : ","Num1 = ",num1,"Num2 = ",num2)
'''
8 7
9 8
8  4 2 1
1  0 0 1
1  0 0 0
0  1 1 1

 
'''