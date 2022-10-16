class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = Counter(t)
        hashmap = Counter()
        bestLeft = used = left = 0
        bestRight = len(s) + 1
        for index in range(len(s)):
            if s[index] not in counter:
                continue
            hashmap[s[index]] += 1
            used += int(hashmap[s[index]] == counter[s[index]])
            while used == len(counter):
                if index - left < bestRight - bestLeft:
                    bestRight = index + 1
                    bestLeft = left
                if s[left] in hashmap:
                    hashmap[s[left]] -= 1
                if hashmap[s[left]] < counter[s[left]]:
                    used -= 1
                left += 1
        return s[bestLeft:bestRight] if bestRight != len(s) + 1 else ''
    
    
            
                