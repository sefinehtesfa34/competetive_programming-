class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        count1 = Counter(word1)
        count2 = Counter(word2)
        for char2 in set(word2):
            count2[char2] -= 1
            if count2[char2] == 0:
                del count2[char2]
            for char1 in set(word1):
                count1[char1] -= 1
                if count1[char1] == 0:
                    del count1[char1] 
                count1[char2] += 1
                count2[char1] += 1
                if len(count1) == len(count2):
                    return True
                count1[char2] -= 1
                count1[char1] += 1
                count2[char1] -= 1
                if count2[char1] == 0:
                    del count2[char1]
                if count1[char2] == 0:
                    del count1[char2]
            count2[char2] += 1
        return False
    
                
        
        
        
        
        
        
        
        
        
        