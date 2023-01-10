class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        hashmap = {}
        seen = set()
        for index, char in enumerate(s):
            hashmap[char] = index
        for index in range(len(s)):
            if s[index] in seen:
                continue
            while stack and stack[-1] > s[index] and hashmap[stack[-1]] > index:
                seen.remove(stack.pop())
            stack.append(s[index])
            seen.add(s[index])
        return ''.join(stack)
    
                