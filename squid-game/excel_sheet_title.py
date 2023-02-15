class Solution:
    def convertToTitle(self, n: int) -> str:
        ans = []
        while(n > 0):
            n -= 1
            curr = n % 26
            n = int(n / 26)
            ans.append(chr(curr + ord('A')))
        
        return ''.join(ans[::-1])