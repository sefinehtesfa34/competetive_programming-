class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for index in range(len(s)):
            if stack and stack[-1] == s[index]:
                stack.pop()
            else:
                stack.append(s[index])
        return "".join(stack)