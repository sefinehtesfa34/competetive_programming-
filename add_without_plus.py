class Solution:
    def add_without_plus(self):
        x, y = list(map(int, input().split()))
        answer = 0
        carry = 0
        for bit in range(32):
            if x & 1<< bit and y & 1 << bit:
                answer |= carry << bit
                carry = 1
            elif x & 1 << bit or y & 1 << bit:
                answer |= (1 - carry) << bit 
                
            elif carry:
                answer |= 1 << bit 
                carry = 0
                
        return answer  
    
            
solution = Solution()
result = solution.add_without_plus()
print(result)
                