import heapq as hq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq.heapify(nums)
        for i in range(len(nums)-k+1):
            poped=hq.heappop(nums)
        return poped