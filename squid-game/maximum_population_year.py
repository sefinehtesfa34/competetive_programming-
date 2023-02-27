class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        prefix = [0]*(2052)
        for birth, death in logs:
            prefix[birth] += 1
            prefix[death] -=1
        for index in range(1950, 2052):
            prefix[index] += prefix[index - 1]
        ans = 0
        max_pop = 0
        for index in range(1950, 2052):
            if prefix[index] > max_pop:
                max_pop = prefix[index]
                ans = index
        return ans