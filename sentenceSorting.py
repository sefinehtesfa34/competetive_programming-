class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split()
        l=[]
        for i in s:
            l.append(i[-1])
        l.sort()
        output=''
        for k in range(len(s)):
            for i in s:
                if i.endswith(l[k]):
                    output+=' '+i[:len(i)-1]
                    break
        return output.strip()