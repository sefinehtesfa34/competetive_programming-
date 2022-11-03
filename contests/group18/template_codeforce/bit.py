from math import *
class Trie:
    def __init__(self) -> None:
        self.children = {}
        self.end = False 
        self.num = 0
class Solution:
    def __init__(self) -> None:
        self.root = Trie()
    def solution(self, bits):
        for bit in bits:
            self.insert(bit)
        for bit in bits:
            self.search(bit)
        
    def insert(self, bit):
        root = self.root 
        for index in range(27):
            cur = bit & 1 << index 
            if cur not in root.children:
                root.children[cur] = Trie()
            root = root.children[cur]
        root.end = True 
        root.num = bit 
             
    def search(self, bit):
        root = self.root 
        result = 0
        for index in range(27):
            curr = bit & 1 << index 
            if curr not in root.children:
                return 0
            for node in root.children:
                if node.end:
                    value = log2(node.num & bit)
                    if 2** value == node.num & bit:
                        result += 1
            root = root.children[curr]
            
        return result 
    
    
     
    
def get_int():
    return int(input())
def get_nums():
    return list(map(int, input().split()))
def main():
    n = get_int()
    bits = []
    for _ in range(n):
        string = input()
        bit = 0
        for char in string:
            bit |= 1 << ord(char) - ord('a')
        bits.append(bit)
    solution = Solution()
    solution.solution(bits)
    
    
        
    
main()