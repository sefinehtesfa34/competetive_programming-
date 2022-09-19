from math import ceil, log2


class Solution:
    def addWithoutOperator(self,x,y):
        carry = 0
        result = 0
        bitSize = ceil(log2(max(x,y) + 1))
        for bit in range(bitSize + 1):
            x_set = int(x & 1 << bit != 0) #If the current bit in x is set (1), x_set = 1 else x_set = 0
            y_set = int(y & 1 << bit != 0) # If the current bit in y is set(1), y_set = 1 else y_set = 0
            if x_set and y_set and carry:
                temp = 3
            elif x_set and y_set or (x_set and carry) or (y_set and carry):
                temp = 2 
            elif x_set or y_set or carry:
                temp = 1
            else:
                temp = 0
            result |= temp % 2 << bit 
            carry = temp //2
            # result |= (x_set + y_set + carry ) % 2 << bit  # If the sum is odd, result at current position could be set
            # carry = (x_set + y_set + carry) // 2
        return result 
      
solution = Solution()
x= int(input())
y = int(input())
result = solution.addWithoutOperator(x,y)
print(result)

