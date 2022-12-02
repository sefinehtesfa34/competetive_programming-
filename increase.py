class Solution:
    def integerReplacement(self, n: int) -> int:
        operations = 0
        while n != 1:
            if n % 2 == 0:
                n //= 2
                operations += 1
                continue 
            operations += 1
            inc_one = n + 1
            dec_one = n - 1
            cur_inc_oper = cur_dec_oper = 0
            while inc_one % 2 == 0:
                inc_one //= 2
                cur_inc_oper += 1
            while dec_one % 2 == 0:
                dec_one //= 2
                cur_dec_oper += 1
            operations += max(cur_dec_oper, cur_inc_oper)
            n = min(dec_one, inc_one)
        return operations
    
solution = Solution()
n = int(input())
result = solution.integerReplacement(n)
print(result)