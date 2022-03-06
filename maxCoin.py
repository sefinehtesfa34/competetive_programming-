class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        val=0
        for i in range(len(piles)):
            if len(piles)>=3:
                piles.pop()
                piles.pop(0)
                mxVal=piles.pop(0)
                val+=mxVal
            else:
                break
        return val
            

            
