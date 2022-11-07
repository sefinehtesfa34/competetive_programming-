class Solution:
    def maximum69Number (self, num: int) -> int:
        
        answer = 0
        first_six_index = -1
        cur_digit = 0
        cur_num = num
        while cur_num:
            remainder = cur_num % 10
            cur_num //= 10
            if remainder == 6:
                first_six_index = cur_digit
            cur_digit += 1
        return num if first_six_index == -1 else num + 3 * 10**first_six_index
    
    
    
    