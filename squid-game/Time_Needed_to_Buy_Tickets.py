class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        n = len(tickets)
        for index in range(n):
            ans += min(tickets[k] - (index > k), tickets[index])
        return ans
    
            