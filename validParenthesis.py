class Solution:
    def isValid(self, s: str) -> bool:
        dictionary={"[":"]","{":"}","(":")"}
        l=[]
        for i in s:
            if i in dictionary.keys():
                l.append(i)
            if i in dictionary.values():
                if len(l)==0:
                    return False
                else:
                    poped=l.pop()
                    if i!=dictionary[poped]:
                        return False
        if len(l)==0:
             return True
                