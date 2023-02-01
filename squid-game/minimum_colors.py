class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        right = 0
        n = len(blocks)
        ans = k
        w = 0
        while right < n:
            w+= int(blocks[right] =='W')
            if right - left + 1== k:
                ans = min(ans, w)
                w-= int(blocks[left] =='W')
                left += 1
            right += 1
        return ans
    
                
                
        
        
        