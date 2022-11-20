class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = Counter()
        max_freq = 0
        left = longest = 0
        for index in range(len(s)):
            hashmap[s[index]] += 1
            max_freq = max(max_freq, hashmap[s[index]])
            is_valid = (index - left + 1) - max_freq <= k
            if not is_valid:
                hashmap[s[left]] -= 1
                left += 1
            longest = index - left + 1
        return longest
    