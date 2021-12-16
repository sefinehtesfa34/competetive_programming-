class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        l=[]
        for i in nums:
            l.append(int(i))
        l.sort()
        l=l[::-1]
        return str(l[k-1])
            