from string import ascii_lowercase
class Solution:
    def appealSum(self, s: str) -> int:
        n = len(s)
        answer = 0
        total_sub = n*(n + 1)//2
        for char in ascii_lowercase:
            count = cur_sub = 0
            for index in range(len(s)):
                if s[index] == char:
                    cur_sub += count*(count + 1) // 2
                    count = -1
                count += 1
            answer += total_sub - cur_sub - count*(count + 1)//2
        return answer
    
                
                