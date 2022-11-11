from collections import defaultdict


class Solution:
    def get_string(self):
        return input()
    
    
    def all_anagrams(self):
        target = self.get_string()
        string = self.get_string()
        answer = []
        frequency = defaultdict(lambda:0)
        for char in target:
            frequency[char] += 1
        for char in string[:len(target)]:
            frequency[char] -= 1
            if frequency[char] == 0:
                del frequency[char]
        
        if not frequency:
            answer.append(0)
        index = len(target)
        while index < len(string):
            frequency[string[index]] -= 1
            frequency[string[index - len(target)]] += 1
            if frequency[string[index - len(target)]] == 0:
                del frequency[string[index - len(target)]]
            if frequency[string[index]] == 0:
                del frequency[string[index]]
            if not frequency:
                answer.append(index - len(target))
            index += 1
        return print(*answer)
    
solution = Solution()
solution.all_anagrams()
            
            
            
            
            
            
            
            
            