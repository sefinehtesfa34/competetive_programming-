class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        unique = set()
        nums = set(nums)
        def count_digit(num):
            count = 0
            while num > 0:
                num //= 10
                count += 1
            return count
        def reverse_num(num):
            count = count_digit(num)
            answer = 0
            while count:
                answer += (num%10)*10**(count-1) 
                num//=10
                count -= 1
            return answer
        for num in nums:
            cur_num = reverse_num(num)
            unique.add(cur_num)
        return len(unique.union(nums))
    
        