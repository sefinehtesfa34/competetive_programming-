class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        cur_sum = 0
        n = len(cardPoints)
        
        for index in range(k):
            cur_sum += cardPoints[index]
            left = index
        
        max_score = cur_sum
        right = len(cardPoints) - 1
        while n - right <= k:
            cur_sum -= cardPoints[left]
            cur_sum += cardPoints[right]
            max_score = max(max_score, cur_sum)
            right -= 1
            left -= 1
        return max_score
    
            
        
        