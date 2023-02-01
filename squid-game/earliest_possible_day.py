class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        
        pair = sorted(zip(plantTime, growTime), key = lambda x:-x[1])
        ans = 0
        cur_sum = 0
        for index in range(len(pair)):
            cur_sum += pair[index][0]
            ans = max(ans, cur_sum + pair[index][1])
        return ans
        
        
        
        