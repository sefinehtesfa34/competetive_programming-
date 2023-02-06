class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key = len)
        n = len(words)
        dp = [1]*(n + 1)
        for right in range(n):
            for left in range(right):
                left_word = words[left]
                right_word = words[right]
                if len(right_word) - len(left_word) != 1:
                    continue
                left_ptr = right_ptr = count = 0
                while left_ptr < len(left_word) and right_ptr < len(right_word):
                    if left_word[left_ptr] != right_word[right_ptr]:
                        right_ptr += 1
                        count += 1
                    else:
                        left_ptr += 1
                        right_ptr += 1
                if count <= 1:
                    dp[right] = max(dp[right], 1 + dp[left])
            
        return max(dp)
                    