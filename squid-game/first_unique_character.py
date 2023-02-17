class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic={}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for key,val in dic.items():
            if val==1:
                return s.index(key)
        return -1