class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        d={}
        lis=[]
        check=0
        for i in range(len(l)):
            sliced=nums[l[i]:r[i]+1]
            sliced.sort()
            val=sliced[1]-sliced[0]
            for j in range(1,len(sliced)-1):
                if sliced[j+1]-sliced[j]!=val:
                    check=1
                    lis.append(False)
                    break
            if not check:
                lis.append(True)
            check=0
        return lis
            
