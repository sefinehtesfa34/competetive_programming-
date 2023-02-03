from math import floor
import random
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.prob = []
        sums = sum(w)
        self.nums = []
        for index, weight in enumerate(w):
            prob = floor((weight/sums)*100)
            self.prob.append(prob)
            for _ in range(prob):
                self.nums.append(index)
        
    def pickIndex(self) -> int:
        if not self.nums:
            return 0
        return random.choice(self.nums)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()