import heapq as hq
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        output=[]
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        values=sorted(dic.items(),key=lambda x:x[1])
        for i in range(k):
            output.append(values[-1-i][0])
        return output
    
    
    
    
    
#         negValues=list(map(self.negative,nums))
#         hq.heapify(negValues)
#         for i in range(k):
#             poped=hq.heappop(negValues)
#             output.append(-1*poped)
        
#     def negative(self,val):
#         return -1*val
