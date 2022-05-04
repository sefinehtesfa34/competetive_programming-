class TrieNode:
    def __init__(self):
        self.children ={}
        self.endofWrod = False 

class Trie:

    def __init__(self):
        
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:         
        
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.endofWrod =True
       
    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            else:
                cur = cur.children[c]
        return cur.endofWrod
  
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            else:
                cur = cur.children[c]
                
        return True
        