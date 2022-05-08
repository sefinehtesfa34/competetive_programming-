class TrieNode:
    def __init__(self):
        self.children =defaultdict(TrieNode)
        self.words=[]

class Solution:
    
    def __init__(self):
        self.root=TrieNode()
    
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        for product in sorted(products):
            self.insert(product)
        return self.find(searchWord)
    
    def insert(self, word):
        cur = self.root
        for letter in word:
            cur = cur.children[letter]
            if len(cur.words)<3: cur.words.append(word)
    
    def find(self,word):
        result=[]    
        cur=self.root
        for letter in word:
            cur=cur.children[letter]
            result.append(cur.words)
        return result
