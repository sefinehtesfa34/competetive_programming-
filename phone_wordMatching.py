from collections import deque
class Solution:
    def __init__(self):
        self.hashmap = {
                2:'abc',
                3:'def',
                4:'ghi',
                5:'jkl',
                6:'mno',
                7:'pqrs',
                8:'tuv',
                9:'wxyz'
                   }
    def match(self,words,digits):
        queue = deque([])
        for word in words:
            if word[0] in self.hashmap[digits[0]] \
                and len(word) == len(digits):
                queue.append(word)
        index = 1 # len(digits) = D AND len(words) = N     
        while index < len(digits):      # O(D) 
            WORD = self.hashmap[digits[index]] 
            for _ in range(len(queue)): # O(N)  Over all => O(N * D) <= Worst case
                front = queue.popleft()   
                if front[index] in WORD:
                    queue.append(front)
            index += 1
        return queue 
    
        # '''
        #         4 ghi 
        #         7 
        #         pqrs 
        #         2   3 
        #         abc def 
        #         5   6 
        #         jkl mno 
        #         8   9 
        #         tuv wxyz 
        # 8733
        # words = {used, tree,tutorial, trade, user, using,vrse}
        # first level:
        #     used tree tutorial, trade, user, using, vrse
        #     used tree trade user using vrse
        #     used tree user 
        #     used tree 
            
        
        
        
        # '''
        
        
solution = Solution()
words = input().split()
digits = list(map(int,input().split()))
result = solution.match(words,digits)
print(result)
