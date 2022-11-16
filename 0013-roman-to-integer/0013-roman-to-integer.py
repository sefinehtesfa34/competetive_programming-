class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        value=0
        for i in range(len(s)):
            if i<len(s)-1:
                if s[i]=='I' and s[i+1]=="V":
                    value-=1
                    continue
                if s[i]=="I" and s[i+1]=="X":
                    value-=1
                    continue
                if s[i]=="X" and s[i+1]=="C":
                    value-=10
                    continue
                if s[i]=="X" and s[i+1]=="L":
                    value-=10
                    continue
                if s[i]=="C" and s[i+1]=="D":
                    value-=100
                    continue
                if s[i]=="C" and s[i+1]=="M":
                    value-=100
                    continue

            value+=dictionary[s[i]]
        return value
sol=Solution()
print(sol.romanToInt("IV"))

        