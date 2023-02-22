class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hashmap = Counter()
        ans = 0
        for index in range(len(time)):
            mod = time[index] % 60
            if mod == 0:
                ans += hashmap[mod]
            ans += hashmap[60-mod]
            hashmap[mod]+= 1
        return ans
    