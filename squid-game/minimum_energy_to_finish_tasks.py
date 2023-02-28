from typing import List
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks = sorted(tasks, key = lambda x:-(x[0] - x[1]))
        low = 0
        high = 10**9
        n = len(tasks)
        def check(energy):
            for index in range(n - 1, -1, -1):
                if energy < tasks[index][1]:
                    return False
                energy -= tasks[index][0]
            return energy >= 0
        while low < high:
            mid = (low + high)>>1
            response = check(mid)
            if response == True:
                high = mid
            else:
                low = mid + 1
        return high