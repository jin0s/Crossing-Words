def ord_(char):
    return ord(char) - ord('A')

class Trie:
    
    def __init__(self):
        self.head = TrieNode('-')
        self.depth_counter = [0]*15
        
    def find_prefix(self, word):
        return self.head.find_prefix(0, word)
    
    def insert_word(self, word):
        self.depth_counter[len(word)] += 1
        self.head.insert_word(0, word)
        
        
class TrieNode:
    
    def __init__(self, cur):
        self.cur_char = cur
        self.next_char = [None]*26
        self.depth_counter = [0]*15
        
    def find_prefix(self, index, word):
        if(len(word) == index):
            return True
        next_node = ord_(word[index])
        if self.next_char[next_node] is None:
            return False
        return self.next_char[next_node].find_prefix(index+1, word)
    
    def insert_word(self, index, word):
        if(len(word) == index):
            return
        self.depth_counter[len(word)-index] += 1
        next_node = ord_(word[index])
        if self.next_char[next_node] is None:
            self.next_char[next_node] = TrieNode(word[index])
        self.next_char[next_node].insert_word(index+1, word)
