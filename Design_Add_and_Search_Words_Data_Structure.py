from queue import deque
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if not ch in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True
        return

    def search(self, word: str) -> bool:
        Q    = deque([self.root]) # use a queue to store all char in one level, used for "."
        for ch in word:
            if ch == ".":
                for _ in range(len(Q)):
                    node = Q.popleft()
                    Q.extend(list(node.children.values()))
            else:
                for _ in range(len(Q)):
                    node = Q.popleft()
                    if ch in node.children:
                        Q.append(node.children[ch])
                if not Q: 
                    return False
        while Q:
            node = Q.popleft()
            if node.is_end:
                return True
            
        return False
    
    
    
    
    
    
    
    
    
    