class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        hashmap = {}
        if len(words) != len(pattern):
            return False
        for index in range(len(pattern)):
            if pattern[index] not in hashmap:
                hashmap[pattern[index]] = words[index]
            elif hashmap[pattern[index]] != words[index]:
                return False
        return len(set(hashmap.values())) == len(hashmap)