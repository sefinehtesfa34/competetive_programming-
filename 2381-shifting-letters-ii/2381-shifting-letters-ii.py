from string import *
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0]*(len(s) + 1)
        result = []
        for start, end, DIR in shifts:
            prefix[start] += 1 if DIR == 1 else -1
            prefix[end + 1] -= 1 if DIR == 1 else -1
        for index in range(1, len(prefix)):
            prefix[index] += prefix[index - 1]
        for index, shift in enumerate(prefix[:-1]):
            index = ascii_lowercase.index(s[index])
            result.append(ascii_lowercase[(shift + index) % 26])
        return "".join(result)
            
        