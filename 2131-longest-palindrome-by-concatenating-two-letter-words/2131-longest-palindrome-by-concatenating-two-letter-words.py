class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        hashmap = Counter()
        unique = set(words)
        answer = 0
        single = False
        for strs in words:
            hashmap[strs] += 1
        values = list(hashmap.items())
        values = sorted(values, key = lambda x:-x[1])
        for strs, count in values:
            if not single and strs[0] == strs[1] and count % 2 == 1:        
                single = True
                answer += count * 2
            
            elif strs[0] == strs[1] and count % 2 == 1:
                answer += (count - 1) * 2
            elif strs[0] == strs[1]:
                answer += count * 2
            else:
                curr_count = min(count, hashmap[strs[::-1]])
                answer += curr_count * 4
                del hashmap[strs]
                del hashmap[strs[::-1]]
        
        return answer
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    