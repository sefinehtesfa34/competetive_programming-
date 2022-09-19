class TrieNode:
    def __init__(self):
        self.children = {}
        
class Solution:
    def __init__(self):
        self.root = TrieNode()
    def isSubstring(self,str1,rotated):
        self.insert(str1)
        for index in range(len(rotated) - 1, -1 ,-1): # O(N) 
            print(rotated[index:])       
            if self.prefix(rotated[index:]): # O(log N)
                if self.checker(index,str1,rotated):  # O(N)
                    return True 
        return False 
    def insert(self,str1):
        cur = self.root 
        for char in str1:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        
    def prefix(self,substr):
        cur = self.root 
        for char in substr:
            if char not in cur.children:
                return False
            cur = cur.children[char] 
        return True  # welcome  length = 7 -  4
    def checker(self,index,str1,rotated):
        subRotated = rotated[:index]
        subStr1 = str1[len(str1) - index:]
        print(subRotated,subStr1)
        return subStr1 == subRotated 
solution = Solution()
str1 = input()
rotated = input()
result = solution.isSubstring(str1,rotated)
print(result)
'''
Time complexity = O(N^2 log N)
water
er wat

'''
    
                
            
        