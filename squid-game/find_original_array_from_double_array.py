class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        dct=collections.Counter(changed)
        
        if dct[0]%2!=0: return []
        res=[]
        for el in sorted(dct):
            while dct[el]>0 and dct[el*2]>0:
                res.append(el)
                dct[el]-=1
                dct[el*2]-=1
        return res if sum(dct.values())==0 else []
    
    