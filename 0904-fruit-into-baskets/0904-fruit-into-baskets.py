class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hashmap = Counter()
        left = longest = 0
        for index in range(len(fruits)):
            hashmap[fruits[index]] += 1
            while len(hashmap) > 2:
                hashmap[fruits[left]] -= 1
                if hashmap[fruits[left]] == 0:
                    del hashmap[fruits[left]]
                left += 1
            longest = max(longest, index - left + 1)
        return longest
    