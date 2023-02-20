class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def get_unique(word, dp):
            unique = []
            left = 0
            for index in range(len(word)):
                if unique and unique[-1] == word[index]:
                    dp[left - 1] += 1
                    continue
                dp[left] = 1
                unique.append(word[index])
                left += 1
            return unique, dp
        dp = [0]*len(s)
        unique, dp = get_unique(s, dp)
        ans = 0
        for word in  words:
            unique_word, cur_dp = get_unique(word, [0]*len(s))
            if unique_word != unique:
                continue
            for index in range(len(unique)):
                if dp[index] < cur_dp[index] \
                    or (dp[index] != cur_dp[index]) and dp[index] < 3:
                    break
            else:
                ans += 1
        return ans
    
    
            
            
            
            
            
            
            
