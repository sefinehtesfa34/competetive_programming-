class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        hashmap = Counter(words)
        answer = 0
        central = False
        for word, count in hashmap.items():
            if word[0] == word[1]:
                if count % 2 == 0:
                    answer += count *  2
                else:
                    answer += (count - 1) * 2
                    central = True
            elif word[0] < word[1]:
                answer += 4 * min(count, hashmap[word[::-1]])
        
        return answer + 2 if central else answer
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    