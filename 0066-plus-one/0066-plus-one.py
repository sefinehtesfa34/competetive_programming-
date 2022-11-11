class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        answer = [0]*(len(digits) + 1)
        index = len(digits) - 1
        carry = 1
        while index >= 0:
            cur_sum = (digits[index] + carry)
            if cur_sum == 10:
                answer[index + 1] = 0
                carry = 1
            else:
                carry = 0
                answer[index + 1] = cur_sum
            index -= 1
        if carry:
            answer[0] = carry
            
        return answer if answer[0] != 0 else answer[1:]