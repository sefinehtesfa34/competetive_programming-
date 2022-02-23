import heapq as hq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic={}
        for i in words:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        listValues=list(dic.values())
        listKeys=list(dic.keys())
        listValues=list(map(self.negative,listValues))
        tupled=zip(listValues,listKeys)
        tupled=list(tupled)
        heapified=[]
        output=[]
        for i in tupled:
            hq.heappush(heapified,i)
        for i in range(k):
            poped=hq.heappop(heapified)
            output.append(poped[1])
        return output
    def negative(self,val):
        return -1*val
    
