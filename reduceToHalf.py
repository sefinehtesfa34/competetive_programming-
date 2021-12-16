class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        l=[]
        dictVal={}
        count=0
        setVal=set(arr)
        setVal=list(setVal)
        for j in range(len(setVal)):
            for i in range(len(arr)):
                if arr[i]==setVal[j]:
                    count+=1
            dictVal[setVal[j]]=count
            count=0
        value=0
        count=0
        for key in dictVal:
            l.append(dictVal[key])
        total=0
        counter=0
        l.sort()
        l=l[::-1]
        for i in l:
            total+=i
            counter+=1
            if total>=len(arr)//2:
                break
        return counter