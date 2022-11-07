class Solution:
    def maximum69Number (self, num: int) -> int:
        
        length, first_index = self.find_length(num)
        if first_index == -1:
            return num
        
        answer = 0
        cur_length = length
        while num:
            remainder = num % 10
            num //= 10
            if length - cur_length + 1 == first_index:
                remainder = 9
            answer += 10 ** (length - cur_length) * remainder
            cur_length -= 1
            
        return answer
    
    
    
    def find_length(self, num):
        
        length = 0
        first_index = -1
        while num:
            remainder = num % 10
            num //= 10
            length += 1
            if remainder == 6:
                first_index = length
            
        return length, first_index
    
        
    
    
    
        