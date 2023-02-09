class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        answer = []
        n = len(s)
        def backtrack(index, temp):
            if len(temp) == 4 and index == n:
                answer.append(".".join(temp))
                return
            if index == len(s) or len(temp) == 4:
                return
            ip =''
            for curr in range(index, len(s)):
                ip += s[curr]
                if int(ip) > 255 or len(ip) > 1 and ip[0] == '0':
                    break
                backtrack(curr + 1, temp + [ip])
        backtrack(0, [])
        return answer
    
                
            