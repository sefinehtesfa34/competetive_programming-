class Solution:
    def isUnique(self,word):
        num = 0
        length = len(word)
        num_set_bit = 0
        for char in word:
            num |= 1<<ord(char) - ord('a')
        for bit in range(26):
            if num & 1<<bit:
                num_set_bit += 1
        return length == num_set_bit 
solution = Solution()
word = input()
result = solution.isUnique(word)
print(result)