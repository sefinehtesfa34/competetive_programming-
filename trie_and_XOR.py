class TrieNode:
    def __init__(self):
        self.children = {}
class Solution:
    def __init__(self):
        self.root = TrieNode()
    def driver(self, nums):
        max_path = 0
        for num in nums:
            self.insert(num)
        for num in nums:
            current = self.search(num)
            max_path = max(current, max_path)
        return max_path 
    
    def insert(self, num):
        cur = self.root
        bitSize = 31
        for bit in range(bitSize,-1,-1):
            
            setUnset= int(num & 1<<bit != 0)
            if setUnset not in cur.children:
                cur.children[setUnset] = TrieNode()
            cur = cur.children[setUnset]
    def search(self,num):
        cur = self.root 
        bitSize = 31
        max_path = 0
        for bit in range(bitSize, -1, -1):
            setUnset = int(num & 1<<bit != 0)
            possible = 0
            if setUnset == 0:
                possible = 1
            if possible in cur.children:
                cur = cur.children[possible]
                max_path |= 1<<bit 
            else:
                cur = cur.children[setUnset]
        return max_path 
solution = Solution()
nums = [1,2,4]
result = solution.driver(nums)
print(result)
'''
    16 8 4 2 1
1    0 0 0 0 1
2    0 0 0 1 0 
3    0 0 0 1 1
4    0 0 1 0 0 
7    0 0 1 1 1
5    0 0 1 0 1
8    0 1 0 0 0
15   0 1 1 1 1
24   1 1 0 0 0 
24 and 7
     1 1 1 1 1 

'''