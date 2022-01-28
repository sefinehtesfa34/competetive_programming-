class Solution:
    def maxArea(self, height: List[int]) -> int:
        pointer1=0
        maxValue=0
        pointer2=len(height)-1
        for i in range(len(height)):
            end=height[pointer2]
            start=height[pointer1]
            
            area=abs(end if end<start else start)*(pointer2-pointer1)
            if area>maxValue:
                maxValue=area
            if end<=start:  
                pointer2-=1
            else:
                pointer1+=1
            if pointer1==pointer2:
                break
        return maxValue
            
