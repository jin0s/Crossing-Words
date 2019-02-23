class Trie:
    
    def __init__(self):
        self.head = TrieNode('-')
        self.max_depth = 0
        
    def find_prefix(self, word):
        return self.head.find_prefix(0, word)
    
    def insert_word(self, word):
        self.head.insert_word(0, word)

class TrieNode:
    
    def __init__(self, cur):
        self.cur_char = cur
        self.next_char = [None]*26
        self.max_depth = 0
        
    def find_prefix(self, index, word):
        return False
    
    def insert_word(self, index, word):
        return
