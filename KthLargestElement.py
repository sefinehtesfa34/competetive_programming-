from heapq import heappush, heapify, heappop
from typing import List
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.heap = nums
        heapify(self.heap)
        while len(self.heap)>k:
            heappop(self.heap)
    def add(self, val: int) -> int:
        heappush(self.heap, val)
        while len(self.heap)>self.k:
            heappop(self.heap)
        return  self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
